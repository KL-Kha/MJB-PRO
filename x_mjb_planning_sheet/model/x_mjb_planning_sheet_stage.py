from odoo import api, fields, models


class XMjbPlanningSheetStage(models.Model):
    _name = "x_mjb_planning_sheet_stage"
    _description = "Planning Sheet Stage"
    _rec_name = "x_name"

    x_active = fields.Boolean(string="Active", default=True)
    x_code = fields.Char(string="Code", required=True)
    x_name = fields.Char(string="Name", required=True)
    x_notes = fields.Text(string="Notes")
    x_sequence = fields.Integer(string="Seq")
