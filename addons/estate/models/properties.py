from odoo import api, fields, models, _
from odoo.exceptions import UserError


class Properties(models.Model):
    _name = 'estate.properties'
    _description = 'Properties'
    _order = "id desc"

    name = fields.Char(required=True)
    property_type_id = fields.Many2one('estate.property.type')
    tag_ids = fields.Many2many('estate.property.tag')
    sale_person_id = fields.Many2one('res.partner', default=lambda self: self.env.user)
    buyer_id = fields.Many2one('res.users', copy=False)
    offer_ids = fields.One2many('estate.property.offer', 'property_id')
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(default=lambda self: fields.Date.today(), copy=False)
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(compute='_compute_selling_price')
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    total_area = fields.Float(compute='_compute_total')
    best_offer = fields.Float(compute='_compute_offer_price')
    garden_orientation = fields.Selection([
        ('north', 'North'),
        ('south', 'South'),
        ('east', 'East'),
        ('west', 'West')
    ], default='north')
    active = fields.Boolean(default=False)
    state = fields.Selection([
        ('new', 'New'),
        ('offer_received', 'Offer Received'),
        ('offer_accepted', 'Offer Accepted'),
        ('sold', 'Sold'),
        ('cancel', 'Canceled')
    ], default='new')

    _sql_constraints = [
        ('check_expected_price_positive', 'CHECK(expected_price > 0)', 'Expected Price must be strictly positive.'),
        ('check_selling_price_positive', 'CHECK(selling_price >= 0)', 'Selling Price must be positive.'),
    ]

    @api.constrains('selling_price')
    def _check_selling_price(self):
        for property_record in self:
            if property_record.selling_price < 0.9 * property_record.expected_price:
                raise UserError(_("Selling Price cannot be lower than 90% of Expected Price."))

    @api.depends('living_area', 'garden_area')
    def _compute_total(self):
        for rec in self:
            rec.total_area = rec.living_area + rec.garden_area

    @api.depends('offer_ids', 'expected_price')
    def _compute_selling_price(self):
        for property_record in self:
            if property_record.offer_ids:
                property_record.selling_price = max(property_record.offer_ids.mapped('price'))
            else:
                property_record.selling_price = 0.0

    @api.depends('offer_ids', "best_offer")
    def _compute_offer_price(self):
        for rec in self:
            best_offer_price = 0.0
            for offer in rec.offer_ids:
                if offer.price > best_offer_price:
                    best_offer_price = offer.price

            rec.best_offer = best_offer_price

    @api.onchange("garden", "garden_area")
    def onchange_garden(self):
        if self.garden:
            self.garden_area = 10

    def action_confirm(self):
        for rec in self:
            rec.state = "sold"

    def action_cancel(self):
        for rec in self:
            if rec.state == "sold":
                raise UserError(_("Action Fail! House is Sold."))
            rec.state = "cancel"
