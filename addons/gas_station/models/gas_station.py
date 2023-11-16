from odoo import api, fields, models


class GasStation(models.Model):
    _name = 'gas.station'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'GasStation'

    name = fields.Char(tracking=True)
    company_id = fields.Many2one("res.company")
    address = fields.Char(tracking=True)
    price_per_unit = fields.Float()
    line_ids = fields.One2many("gas.station.line", "station_id")
    status = fields.Selection([
        ('available', 'Available'),
        ('in_use', 'In Use'),
        ('maintenance', 'Under Maintenance')], default='available')

