from odoo import api, fields, models, _


class SaleOrderLine(models.Model):
    _name = 'liquor.order.line'
    _description = 'Liquor Order Line'

    order_id = fields.Many2one('liquor.order', string='Sale Order', default=lambda self: _("New"))
    product_id = fields.Many2one('liquor.product', string='Product')
    quantity = fields.Integer(string='Quantity')
    company_id = fields.Many2one('res.company', default=lambda self: self.env.user.company_id.id)
    currency_id = fields.Many2one('res.currency', related='company_id.currency_id')
    price = fields.Monetary(string='Price')
    total = fields.Monetary(string='Total Amount')
