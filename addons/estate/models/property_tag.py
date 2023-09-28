from odoo import api, fields, models


class PropertyTag(models.Model):
    _name = 'estate.property.tag'
    _description = 'PropertyTag'
    _order = 'name desc'

    name = fields.Char()
    color = fields.Integer()

    _sql_constraints = [
        ('unique_tag_name', 'UNIQUE(name)', 'Tag Name must be unique.'),
    ]

