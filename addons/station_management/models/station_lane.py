from odoo import api, fields, models


class StationManagementLane(models.Model):
    _name = 'station.management.lane'
    _description = 'StationManagementLane'

    name = fields.Char()
    station_id = fields.Many2one('station.management')
    active = fields.Boolean()
    color = fields.Integer(string='Color')
