from odoo import http
from odoo.http import request

class LibraryDashboardController(http.Controller):

    @http.route('/library/dashboard/stats',  type='json', auth='public', csrf=False)
    def get_stats(self):
        total = request.env['library.book'].sudo().search_count([])
        borrowed = request.env['library.book'].sudo().search_count([('state', '=', 'borrowed')])
        available = request.env['library.book'].sudo().search_count([('state', '=', 'available')])
        return {'total_books': total, 'borrowed_books': borrowed, 'available_books': available}
