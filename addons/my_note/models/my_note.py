from odoo import api, fields, models


class Note(models.Model):
    _name = 'my.note'
    _description = 'Note'

    title = fields.Char()
    description = fields.Text()

