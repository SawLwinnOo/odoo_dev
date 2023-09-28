from odoo import http
from odoo.http import request


class MyController(http.Controller):
    @http.route('/', website=True, auth='public')
    def products(self):
        products = request.env['liquor.product'].search([])

        return request.render("liquor.product_page", {"products": products})
