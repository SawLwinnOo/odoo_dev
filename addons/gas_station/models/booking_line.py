from odoo import api, fields, models


class BookingLine(models.Model):
    _name = 'gas.booking.line'
    _description = 'BookingLine'

    start_time = fields.Datetime()
    end_time = fields.Datetime()
    units = fields.Integer()
    total = fields.Float(compute='_compute_subtotal')
    booking_id = fields.Many2one("gas.booking")
    car_id = fields.Many2one("gas.car")
    station_id = fields.Many2one("gas.station")

    @api.depends('station_id')
    def _compute_subtotal(self):
        for rec in self:
            rec.total = rec.station_id.price_per_unit * rec.units


