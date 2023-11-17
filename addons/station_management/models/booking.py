from odoo import api, fields, models, _


class StationBooking(models.Model):
    _name = 'station.booking'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Station_Booking'

    name = fields.Char(default=lambda self: _("New"))
    car_id = fields.Many2one("fleet.vehicle", string="Car", tracking=True)
    customer = fields.Char(related='car_id.license_plate', string="Customer")
    station_id = fields.Many2one("station.management", string="Station")
    line_name = fields.Char(required=True)
    booking_date = fields.Datetime(default=lambda self: fields.Datetime.today())
    unit = fields.Float(required=True)
    total = fields.Float(compute="_compute_total")
    note = fields.Html()
    status = fields.Selection([
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('canceled', 'Canceled')
    ], default='pending')

    @api.model
    def create(self, values):
        if values.get('name', _('New')) == _('New'):
            values['name'] = self.env['ir.sequence'].next_by_code('station.booking') or _('New')
        return super(StationBooking, self).create(values)

    @api.depends('unit')
    def _compute_total(self):
        """Compute function for the Amenities"""
        for booking in self:
            booking.total = booking.station_id.price_pre_unit * booking.unit
