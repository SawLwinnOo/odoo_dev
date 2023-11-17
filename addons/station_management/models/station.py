from odoo import api, fields, models


class StationManagement(models.Model):
    _name = 'station.management'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'StationManagement'

    name = fields.Char()
    company_id = fields.Many2one('res.company', default=lambda self: self.env.user.company_id.id)
    location = fields.Char(default=lambda self: self.env.user.contact_address)
    phone = fields.Char(default=lambda self: self.env.user.phone)
    email = fields.Char(default=lambda self: self.env.user.email)
    website = fields.Char(default=lambda self: self.env.user.website)
    line_no = fields.Integer(string="Line Number")
    price_pre_unit = fields.Float()
    special_offer = fields.Float()



