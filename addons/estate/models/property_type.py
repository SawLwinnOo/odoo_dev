from odoo import api, fields, models


class PropertyType(models.Model):
    _name = 'estate.property.type'
    _description = 'PropertyType'
    _order = "name desc"

    name = fields.Char(required=True)
    property_ids = fields.One2many('estate.properties', "property_type_id")
    sequence = fields.Integer('Sequence', default=1)

    _sql_constraints = [
        ('unique_type_name', 'UNIQUE(name)', 'Type Name must be unique.'),
    ]


