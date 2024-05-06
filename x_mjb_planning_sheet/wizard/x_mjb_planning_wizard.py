from odoo import api, fields, models


class XMjbPlanningWizard(models.TransientModel):
    _name = "x_mjb_planning_wizard"
    _description = "Planning Wizard"

    x_name = fields.Char(string="Name")
    x_need_line_ids = fields.Many2many('x_mjb_planning_sheet_line', string="Need Lines")
    x_notes = fields.Text(string="Notes")
    x_product_ids = fields.Many2many('product.product', string="Product Lines")
    x_sale_order_id = fields.Many2one('sale.order', string="Order")
    x_sale_order_line_ids = fields.Many2many('sale.order.line', string="Order Lines")
    x_sheet_id = fields.Many2one('x_mjb_planning_sheet', string="Sheet")
    x_type = fields.Char(string="Type")

