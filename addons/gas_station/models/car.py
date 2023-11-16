from odoo import api, fields, models


class Car(models.Model):
    _name = 'gas.car'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Car'

    name = fields.Char(tracking=True)
    license_no = fields.Char(string="License", tracking=True)
    driver_id = fields.Many2one("res.partner")
