from odoo import http
from odoo.http import request


class Main(http.Controller):
    @http.route('/books', auth='public', type='http', website=True)
    def books(self):
        books  = request.env['library.book'].search([])

        return request.render('my_library.books', {'books': books})

    @http.route('/books/<model("library.book"):book>', auth='public', type='http', website=True)
    def book_detail(self, book):
        return request.render('my_library.book_detail', {'book': book})