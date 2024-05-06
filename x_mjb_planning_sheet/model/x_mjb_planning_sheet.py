from odoo import api, fields, models
from pprint import pprint


class XMjbPlanningSheet(models.Model):
    _name = "x_mjb_planning_sheet"
    _inherit = ['mail.thread', 'mail.activity.mixin', 'utm.mixin']
    _description = "Planning Sheet"
    _rec_name = "x_name"

    x_active = fields.Boolean(string="Active", default=True)
    x_buy_line_ids = fields.One2many('x_mjb_planning_sheet_line', 'x_sheet_id', string="Components", domain=[('x_type', '=', 'buy')])
    x_code = fields.Char(string="Code")
    x_company_id = fields.Many2one('res.company', string="Company")
    x_computed_date = fields.Datetime(string="Compute Date")
    x_date = fields.Date(string="Date")
    x_kit_line_ids = fields.One2many('x_mjb_planning_sheet_line', 'x_sheet_id', string="Kit", domain=[('x_type', '=', 'phantom')])
    x_manufacture_line_ids = fields.One2many('x_mjb_planning_sheet_line', 'x_sheet_id', string="Manufacture", domain=[('x_type', '=', 'manufacture')])
    x_mrp_production_count = fields.Integer(string="Mrp Production Count", compute="_compute_x_mrp_production_count")
    x_name = fields.Char(string="Name", required=True, copy=False, readonly=True, default="New")
    x_notes = fields.Text(string="Notes")
    x_output_line_ids = fields.One2many('x_mjb_planning_sheet_line', 'x_sheet_id', string="Output", domain=[('x_type', '=', 'output')])
    x_production_ids = fields.One2many('mrp.production', 'x_sheet_id', string="Manufacturing Orders")
    x_purchase_order_count = fields.Integer(string="Purchase Order Count", compute="_compute_x_purchase_order_count")
    x_purchase_order_ids = fields.One2many('purchase.order', 'x_sheet_id', string="Purchase Orders")
    x_purchase_order_line_ids = fields.One2many('purchase.order.line', 'x_sheet_id', string="Purchase Order Line")
    x_sale_order_ids = fields.Many2many('sale.order', string="Orders")
    x_sequence = fields.Integer(string="Seq")
    x_stage_id = fields.Many2one('x_mjb_planning_sheet_stage', string="Stage")
    x_stage_code = fields.Char(string="Stage Code", related="x_stage_id.x_code", readonly=True)
    x_subcontract_line_ids = fields.One2many('x_mjb_planning_sheet_line', 'x_sheet_id', string="Subcontract", domain=[('x_type', '=', 'subcontract')])

    # def write(self, vals):
    #     if 'x_output_line_ids' in vals:
    #         return super(XMjbPlanningSheet, self).write(vals)
    #     if 'x_sale_order_ids' in vals:
    #         vals['x_output_line_ids'] = []
    #         sale_order_line_id = [rec.id for rec in self.env['x_mjb_planning_sheet_line'].search([('x_active', '=', 1)])
    #                               if rec.x_sale_order_line_id]
    #         for i in sale_order_line_id:
    #             vals['x_output_line_ids'].append((2, i, 0))
    #         sale_order_ids = vals['x_sale_order_ids'][0][2]
    #         for i in range(len(sale_order_ids)):
    #             sale_order = self.env['sale.order'].browse(vals['x_sale_order_ids'][0][2][i])
    #             for j in range(len(sale_order.order_line)):
    #                 val_sale_order = {
    #                     'x_sale_order_line_id': sale_order.order_line[j].id,
    #                     'x_product_id': sale_order.order_line[j].product_id.id,
    #                     'x_quantity': sale_order.order_line[j].product_uom_qty,
    #                     'x_unit_price': sale_order.order_line[j].price_unit,
    #                     'x_currency_id': sale_order.order_line[j].currency_id.id,
    #                     'x_type': 'output',
    #                 }
    #                 vals['x_output_line_ids'].append((0, 0, val_sale_order))
    #         return super(XMjbPlanningSheet, self).write(vals)
    #     return super(XMjbPlanningSheet, self).write(vals)

    def _compute_x_purchase_order_count(self):
        for record in self:
            record['x_purchase_order_count'] = self.env['purchase.order'].search_count([('x_sheet_id', '=', record.id)])

    def _compute_x_mrp_production_count(self):
        for record in self:
            record['x_mrp_production_count'] = self.env['mrp.production'].search_count([('x_sheet_id', '=', record.id)])

    def action_open_purchase_order(self):
        return {
            'name':'Purchases',
            'view_mode':'tree,form',
            'res_model':'purchase.order',
            'type':'ir.actions.act_window',
            'domain': [('x_sheet_id', '=', self.id)],
            'target':'current',
            'context': {
                'search_default_x_sheet_id': self.id,
                'default_x_sheet_id': self.id},
        }

    def action_open_mrp_production(self):
        return {
            'name': 'Manufacture',
            'view_mode':'tree,form',
            'res_model':'mrp.production',
            'type':'ir.actions.act_window',
            'domain': [('x_sheet_id', '=', self.id)],
            'target':'current',
            'context': {
                'search_default_x_sheet_id': self.id,
                'default_x_sheet_id': self.id},
        }







