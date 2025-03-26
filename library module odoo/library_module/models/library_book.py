from datetime import timedelta
from odoo import models, fields,api
import logging
_logger = logging.getLogger(__name__)
class LibraryBook(models.Model):
    _name = 'library.book' 
    _inherit = ['mail.thread'] # This defines the name of the model

    name = fields.Char(required=True)  # The title of the book
    author = fields.Char(required=True)  # The author of the book
    state = fields.Selection([  # The state of the book: draft, available, or borrowed
        ('draft', 'Draft'),
        ('available', 'Available'),
        ('borrowed', 'Borrowed'),
    ], default='draft')
    borrower_id = fields.Many2one('res.partner', string="Borrower")
    borrow_date = fields.Date(string="Borrow Date")
    fee_per_day = 0.5
    return_date = fields.Date(string="Return Date")
    reservation_id = fields.Many2one('res.partner', string="Reserved By")
    reservation_date = fields.Date(string="Reservation Date")
    late_fees = fields.Float(compute="_compute_late_fees", string="Late Fees")
    category_id = fields.Many2one('library.book.category', string="Category")
    late_fees = fields.Float(compute="_compute_late_fees", string="Late Fees", store=False)
    def _compute_late_fees(self):
        for record in self:
            if record.state == 'borrowed' and record.return_date:
                today = fields.Date.today()
                if record.return_date < today:
                    overdue_days = (today - record.return_date).days
                    record.late_fees = overdue_days * self.fee_per_day  # Define a fee per day
                else:
                    record.late_fees = 0
            else:
                record.late_fees = 0
    def borrow_book_action(self):
        """Called by the button in the form view."""
        for record in self:
            if record.state != 'available':
                raise UserError("Book is not available for borrowing.") # type: ignore
            record.borrow_date = fields.Date.context_today(self)
            record.return_date = record.borrow_date + timedelta(days=7)
            record.state = 'borrowed'

            
            _logger.info("Triggering email for book borrow: %s", self.name)
            template = self.env.ref('library_module.book_borrowed_email_template')
            _logger.info("Using email template: %s", template.name)
            self.env['mail.template'].browse(template.id).send_mail(self.id, force_send=True)
    def return_book(self):
        self.state = 'available'
        self.borrower_id = False
        self.borrow_date = False
        self.return_date = False    
    @api.model
    def check_overdue_books(self):
        today = fields.Date.today()
        overdue_books = self.search([
            ('state', '=', 'borrowed'),
            ('return_date', '<', today)
        ])
        template = self.env.ref('library_module.book_borrowed_notification_template')
        for book in overdue_books:
            if book.borrower_id and book.borrower_id.email:
                _logger.info("Sending overdue email to: %s", book.borrower_id.email)
                template.send_mail(book.id, force_send=True)
    
    
    




class LibraryBookCategory(models.Model):
    _name = 'library.book.category'
    name = fields.Char(string="Category Name")
   
class LibraryBookReview(models.Model):
    _name = 'library.book.review'
    book_id = fields.Many2one('library.book', string="Book")
    user_id = fields.Many2one('res.partner', string="User")
    rating = fields.Integer(string="Rating", required=True)
    review_text = fields.Text(string="Review")
    @classmethod
    def create_review_dialog(cls):
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'library.book.review',
            'view_mode': 'form',
            'view_id': cls.env.ref('library_module.view_library_book_review_form').id,
            'target': 'new',
            'context': {},
        }
    