from odoo import api, fields, models


class XMjbPlanningSheetOpt(models.Model):
    _name = "x_mjb_planning_sheet_opt"
    _description = "Planner Option"
    _rec_name = "x_name"

    x_active = fields.Boolean(string="Active", default=True)
    x_code = fields.Char(string="Code")
    x_company_id = fields.Many2one('res.company', string="Company")
    x_name = fields.Char(string="Name")
    x_notes = fields.Text(string="Notes")
    x_sequence = fields.Integer(string="Seq")
