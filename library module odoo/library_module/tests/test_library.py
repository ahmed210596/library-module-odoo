from odoo.tests.common import TransactionCase

class TestLibrary(TransactionCase):
    def test_create_book(self):
        book = self.env['library.book'].create({
            'name': 'Test Book',
            'author': 'Test Author',
        })
        self.assertEqual(book.state, 'draft')
