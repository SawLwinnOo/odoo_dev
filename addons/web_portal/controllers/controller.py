from odoo import http
from odoo.http import request
from odoo.addons.portal.controllers import portal


class Main(http.Controller):

    @http.route("/my/product", auth='public', website=True)
    def show_product(self, **kwargs):
        products = request.env['product.template'].search([])

        return request.render('web_portal.show_product', {'products': products})


# Portal Extend Class
class CustomerPortal(portal.CustomerPortal):

    # Query Product Count by method overriding from portal module
    def _prepare_home_portal_values(self, counters):
        values = super()._prepare_home_portal_values(counters)
        if 'product_count' in counters:
            invoice_count = request.env['product.template'].search_count([])
            values['product_count'] = invoice_count
        return values

    @http.route(['/my/product-checkouts', '/my/product-checkouts/page/<int:page>'], auth="public", website=True)
    def portal_my_product(self, **kwargs):
        products = request.env['product.template'].search([])

        return request.render("web_portal.portal_products", {'products': products})
