from odoo import api, fields, models, _


class StationBooking(models.Model):
    _name = 'station.booking'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Station_Booking'

    name = fields.Char(default=lambda self: _("New"))
    customer = fields.Many2one('res.partner',string="Customer")
    car_id = fields.Many2one("fleet.vehicle", string="Car", tracking=True, )
    station_id = fields.Many2one("station.management", string="Station", tracking=True)
    lane_id = fields.Many2one('station.management.lane')
    booking_date = fields.Datetime(default=lambda self: fields.Datetime.today(), tracking=True)
    unit = fields.Float(required=True)
    currency_id = fields.Many2one('res.currency', related='station_id.currency_id')
    price = fields.Monetary(related='station_id.price_per_unit')
    total = fields.Monetary(compute="_compute_total")
    note = fields.Html()
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirmed'),
        ('paid', 'Paid'),
        ('accept', 'Accepted'),
        ('arrive', 'Arrived'),
        ('complete', 'Completed'),
        ('reschedule', 'Reschedule'),
        ('cancel', 'Canceled'),

    ], default='draft', tracking=True)

    @api.model
    def create(self, values):
        if values.get('name', _('New')) == _('New'):
            values['name'] = self.env['ir.sequence'].next_by_code('station.booking') or _('New')
        return super(StationBooking, self).create(values)

    @api.depends('unit')
    def _compute_total(self):
        """Compute function for the Amenities"""
        for booking in self:
            booking.total = booking.price * booking.unit

    def action_confirm(self):
        for rec in self:
            rec.state = 'confirm'

    def action_draft(self):
        for rec in self:
            rec.state = 'draft'

    def action_cancel(self):
        for rec in self:
            rec.state = 'cancel'

    def action_paid(self):
        for rec in self:
            rec.state = 'paid'

    def action_accepted(self):
        for rec in self:
            rec.state = 'accept'

    def action_complete(self):
        for rec in self:
            rec.state = 'complete'

    def action_reschedule(self):
        for rec in self:
            rec.state = 'reschedule'

    def action_arrived(self):
        for rec in self:
            rec.state = 'arrive'
