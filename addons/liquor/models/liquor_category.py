from odoo import api, fields, models


class LiquorCategory(models.Model):
    _name = 'liquor.category'
    _description = 'LiquorCategory'

    name = fields.Char(string="Category Name", required=True)

