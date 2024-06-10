from odoo import fields, models, _, api


class AccountAccount(models.Model):
    _inherit = "account.account"

    china_account_type = fields.Many2one('china.account.type', string="China Account Type", help="Information field for CN financial report")


class AccountAccountTemplate(models.Model):
    _inherit = "account.account.template"

    china_account_type = fields.Many2one('china.account.type', string="China Account Type", help="Information field for CN financial report")


class ChinaAccountType(models.Model):
    _name = "china.account.type"
    _description = "China Account Type"

    name = fields.Char(required=True, translate=True)
    code = fields.Char(required=True)
