from odoo import api, fields, models


class StationLine(models.Model):
    _name = 'gas.station.line'
    _description = 'StationLine'

    station_id = fields.Many2one('gas.station')

