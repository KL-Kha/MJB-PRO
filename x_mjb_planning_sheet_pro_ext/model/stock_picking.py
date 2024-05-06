from odoo import api, fields, models


class Picking(models.Model):
    _inherit = "stock.picking"

    x_stage_id = fields.Many2one('x_mjb_planning_sheet_stage', string="Stage")
    x_sheet_id = fields.Many2one('x_mjb_planning_sheet', string="Sheet")


class StockMove(models.Model):
    _inherit = "stock.move"

    x_sheet_id = fields.Many2one('x_mjb_planning_sheet', string="Sheet")
    x_sheet_line_id = fields.Many2one(
        'x_mjb_planning_sheet_line', string="Sheet Line")
    x_stage_id = fields.Many2one('x_mjb_planning_sheet_stage', string="Stage")


class StockMoveLine(models.Model):
    _inherit = "stock.move.line"

    x_sheet_id = fields.Many2one(related="move_id.x_sheet_id")
    x_sheet_line_id = fields.Many2one(related="move_id.x_sheet_line_id")
    x_stage_id = fields.Many2one(related="move_id.x_stage_id")
