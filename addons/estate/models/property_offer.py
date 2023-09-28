from odoo import api, fields, models, _
from odoo.exceptions import UserError
from datetime import timedelta


class PropertyOffer(models.Model):
    _name = 'estate.property.offer'
    _description = 'PropertyOffer'
    _order = "price desc"

    price = fields.Float()
    validity = fields.Integer(default=7)
    date_deadline = fields.Date(string="Deadline", compute='_compute_date_deadline', inverse="_set_date_or_validity")
    partner_id = fields.Many2one('res.partner', required=True)
    property_id = fields.Many2one('estate.properties', required=True)
    status = fields.Selection([
        ('accepted', 'Accepted'),
        ('refused', 'Refused'),
    ],copy=False)

    _sql_constraints = [
        ('check_offer_price_positive', 'CHECK(price > 0)', 'Offer Price must be strictly positive.'),
    ]

    @api.onchange('status')
    def onchange_state(self):
        ...


    @api.depends('create_date', 'validity')
    def _compute_date_deadline(self):
        for offer in self:
            if offer.create_date and offer.validity:
                offer.date_deadline = offer.create_date + timedelta(days=offer.validity)

    def _set_date_or_validity(self):
        for offer in self:
            if offer.date_deadline and offer.create_date:
                offer.validity = (offer.date_deadline - offer.create_date).days

    # Other fields and methods
