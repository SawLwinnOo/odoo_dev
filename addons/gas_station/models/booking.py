from odoo import api, fields, models, _


class GasBooking(models.Model):
    _name = 'gas.booking'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'GasBooking'

    name = fields.Char(default=_("New"))
    car_id = fields.Many2one("gas.car", tracking=True)
    booking_date = fields.Date(default=lambda self: fields.Date.today())
    state = fields.Selection([
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('canceled', 'Canceled')
    ], default='pending')
    booking_line_ids = fields.One2many('gas.booking.line', 'booking_id')
    tax_totals = fields.Float(compute='_compute_total_amount')
    note = fields.Html()

    @api.model
    def create(self, values):
        if values.get('name', _('New')) == _('New'):
            values['name'] = self.env['ir.sequence'].next_by_code('gas.booking') or _('New')
        return super(GasBooking, self).create(values)

    @api.depends('booking_line_ids.total')
    def _compute_total_amount(self):
        for booking in self:
            booking.tax_totals = sum(line.total for line in booking.booking_line_ids)
