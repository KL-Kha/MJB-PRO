from odoo import fields, models, api, _


class AccountAccountTag(models.Model):
    _inherit = "account.account.tag"

    x_code = fields.Char(string="Tag Code")
