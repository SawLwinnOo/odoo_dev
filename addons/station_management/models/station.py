from odoo import api, fields, models


class StationManagement(models.Model):
    _name = 'station.management'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'StationManagement'

    name = fields.Char()
    lane_id = fields.Many2many('station.management.lane', 'station_id')
    owner_id = fields.Many2one("res.users")
    manager_id = fields.Many2one('res.partner')
    employee_id = fields.Many2one("res.partner")
    company_id = fields.Many2one('res.company', default=lambda self: self.env.user.company_id.id)
    currency_id = fields.Many2one('res.currency', related='company_id.currency_id')
    price_per_unit = fields.Monetary(string="Price")




