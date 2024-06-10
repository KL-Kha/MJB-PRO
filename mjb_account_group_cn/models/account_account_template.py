from odoo import fields, models, api, _


class AccountAccountTemplate(models.Model):
    _inherit = "account.account.template"

    group_id = fields.Many2one('account.group.template', readonly=True)
