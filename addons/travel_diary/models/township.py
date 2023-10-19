from odoo import api, fields, models

class TravelTownships(models.Model):
    _name = 'travel.township'
    _description = 'Townships'

    name = fields.Char()
    region =fields.Char()
    country= fields.Char()

