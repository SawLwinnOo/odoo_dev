from odoo import api, fields, models

class travelDiary(models.Model):
    _name = 'travel.diary'
    _description = 'travelDiary'

    name = fields.Many2one('res.partner', required=True)
    nrc_no = fields.Char()
    travel_to = fields.Many2one('travel.township',)
    travel_from = fields.Many2one('travel.township')
