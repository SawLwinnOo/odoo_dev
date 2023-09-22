from odoo import http
from odoo.http import request


class MyController(http.Controller):
    @http.route('/home', website=True, auth='public')
    def product(self):
        return request.render("liquor.product_page", {})
