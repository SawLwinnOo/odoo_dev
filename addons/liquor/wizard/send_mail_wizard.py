from odoo import api, fields, models


class SendMailWizard(models.TransientModel):
    _name = 'send.mail.wizard'

    _description = 'SendMailWizard'

    subject = fields.Char()
    body = fields.Html()
