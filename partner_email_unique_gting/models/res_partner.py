from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class ResPartner(models.Model):
    _inherit = 'res.partner'

    _sql_constraints = [
        ('email_unique', 'unique(email)', 'Контакт з таким Email вже існує!')
    ]

    @api.constrains('email')
    def _check_email_unique(self):
        for record in self:
            if record.email:
                duplicate = self.search([
                    ('id', '!=', record.id),
                    ('email', '=', record.email)
                ], limit=1)
                if duplicate:
                    raise ValidationError(_("Партнер з email %s вже зареєстрований!") % record.email)