from odoo import api, fields, models, _


class LiquorOrder(models.Model):
    _name = 'liquor.order'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'LiquorOrder'

    liquor_order = fields.One2many('liquor.order.line', 'order_id',
                                   string='Liquor Order Lines', tracking=True)
    number = fields.Char(default=lambda self: _("New"), copy=False)
    order_date = fields.Date(default=lambda self: fields.Date.today())
    partner_id = fields.Many2one('res.partner', string='Customer')
    user_id = fields.Many2one('res.users', string='Sale Person')
    state = fields.Selection([
        ('draft','Draft'),
        ('sent','Sent'),
        ('sale', 'Sale Order'),
        ('done', 'Done'),
        ('cancel', 'Canceled')
    ],)
    currency_id = fields.Many2one('res.currency',related='liquor_order.currency_id')
    tax_totals = fields.Monetary()

    @api.model
    def create(self, values):
        if values.get('number', _('New')) == _('New'):
            values['number'] = self.env['ir.sequence'].next_by_code('liquor.order') or _('New')
        return super(LiquorOrder, self).create(values)

    def name_get(self):
        return [(self.id, f"{rec.number}({rec.order_date})") for rec in self]

    def action_draft(self):
        for rec in self:
            rec.state = 'draft'

    def action_confirm(self):
        for rec in self:
            rec.state = 'sale'

    def action_cancel(self):
        for rec in self:
            rec.state = 'cancel'

    def action_send_mail(self):
        template = self.env.ref('')
        for rec in self:
            template.send_mail(rec.id)



