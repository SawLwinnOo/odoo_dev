from odoo import api, fields, models, _
from odoo.exceptions import UserError


class LiquorProduct(models.Model):
    _name = 'liquor.product'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Liquor Product'

    name = fields.Char(string='Product Name', required=True, tracking=True)
    photo = fields.Image()
    category_id = fields.Many2one('liquor.category', string='Category')
    company_id = fields.Many2one("res.company", default=lambda self: self.env.user.company_id.id)
    currency_id = fields.Many2one('res.currency', related="company_id.currency_id")
    price = fields.Monetary()
    stock_qty = fields.Integer(string='Stock Quantity', computed='_compute_stock_qty')
    description = fields.Text(string='Description', tracking=True)
    order_line_id = fields.Many2one("liquor.order.line")
    order_id = fields.Many2one('liquor.order')
    priority = fields.Selection([
        ('1', 'Lower'),
        ('2', 'Low'),
        ('3', 'Normal'),
        ('4', 'High'),
        ('5', 'Highest'),
    ])

    @api.depends('order_id')
    def _compute_stock_qty(self):
        for rec in self.order_id:
            if rec.state == 'sale':
                rec.stock_qty -= rec.liquor_order.quantity

            else:
                rec.stock_qty = 1
