from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    x_stage_id = fields.Many2one('x_mjb_planning_sheet_stage', string="Stage")
