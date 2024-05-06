from odoo import api, fields, models


class MrpProduction(models.Model):
    _inherit = "mrp.production"

    x_sheet_id = fields.Many2one('x_mjb_planning_sheet', string="Sheet")
    x_planner_sheet_line_id = fields.Many2one('x_mjb_planning_sheet_line', string="Sheet Line")
    x_stage_id = fields.Many2one('x_mjb_planning_sheet_stage', string="Stage")
