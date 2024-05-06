from odoo import api, fields, models


class XMjbAlternativeProduct(models.Model):
    _name = "x_mjb_alternative_product"

    x_bom_id = fields.Many2one('mrp.bom', string="BOM")
    x_bom_line_id = fields.Many2one('mrp.bom.line', string="BOM Line")
    x_confirmed_product_id = fields.Many2one('product.product', string="Confirmed Product")
    x_planning_sheet_id = fields.Many2one('x_mjb_planning_sheet', string="Planning Sheet")
    x_product_id = fields.Many2one('product.product', string="Product")
    x_replace_product_ids = fields.Many2many('product.product', string="Replace Product")
