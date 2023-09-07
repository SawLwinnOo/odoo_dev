from odoo import api, fields, models


class SendMailWizard(models.TransientModel):
    _name = 'send.mail.wizard'
    _description = 'SendMailWizard'

    order_id = fields.Many2one('liquor.order')

