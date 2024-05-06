from odoo import api, fields, models


class XMjbPlanningWizard(models.TransientModel):
    _inherit = "x_mjb_planning_wizard"

    x_operation_type_id = fields.Many2one('stock.picking.type', string="Operation Type")
    x_subcontractor = fields.Many2one('res.partner', string="Subcontractor")

