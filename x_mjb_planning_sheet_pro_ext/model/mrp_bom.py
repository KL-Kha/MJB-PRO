from odoo import api, fields, models


class MrpBomLine(models.Model):
    _inherit = "mrp.bom.line"

    x_confirmed_product_id = fields.Many2one('product.product', string="Confirmed Product")
    x_replace_product_ids = fields.Many2many('product.product', string="Alternative Components")
    