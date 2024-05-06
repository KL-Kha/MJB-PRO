from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    x_sheet_id = fields.Many2one('x_mjb_planning_sheet', string="Sheet")

class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    x_sheet_id = fields.Many2one('x_mjb_planning_sheet', string="Sheet")
    x_sheet_line_id = fields.Many2one('x_mjb_planning_sheet_line', string="Sheet Line")
    x_stage_id = fields.Many2one('x_mjb_planning_sheet_stage', string="Stage")

