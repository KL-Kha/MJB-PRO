from odoo import api, fields, models
from pprint import pprint


class XMjbPlanningSheet(models.Model):
    _inherit = "x_mjb_planning_sheet"

    x_default_product_ids = fields.One2many('x_mjb_alternative_product', 'x_planning_sheet_id', string="Alternative Choices")
    x_purchase_order_line_ids = fields.One2many('purchase.order.line', 'x_sheet_id', string="Purchase Order Line", domain=[('order_id.state', '!=', 'cancel')])
    x_resupply_line_ids = fields.One2many('x_mjb_planning_sheet_line', 'x_sheet_id', string="Output", domain=[('x_type', '=', 'resupply')])
    x_sale_line_ids = fields.One2many('x_mjb_planning_sheet_line', 'x_sheet_id', string="Output", domain=[('x_type', '=', 'sell')])
    x_sale_order_count = fields.Integer(string="Sales Order Count", compute="_compute_x_sale_order_count")
    x_sale_order_line_ids = fields.One2many('sale.order.line', 'x_sheet_id', string="Sales Order Line")
    x_stock_move_count = fields.Integer(string="Stock Move Count", compute="_compute_x_stock_move_count")
    x_stock_move_ids = fields.One2many('stock.move', 'x_sheet_id', string="Stock Move")
    x_stock_move_line_ids = fields.One2many('stock.move.line', 'x_sheet_id', string="Stock Move Line")

    def _compute_x_sale_order_count(self):
        for record in self:
            record['x_sale_order_count'] = self.env['sale.order'].search_count([('x_sheet_id', '=', record.id)])

    def _compute_x_stock_move_count(self):
        for record in self:
            picking_type_id = self.env['x_mjb_planning_sheet_opt'].search([('x_code', '=', 'RESUPPLY_OPERATION_TYPE_ID'), ('x_company_id', '=', record.x_company_id.id)])
            record['x_stock_move_count'] = self.env['stock.picking'].search_count([('x_sheet_id', '=', record.id), ('picking_type_id', '=', int(picking_type_id.x_name))])

    def action_open_sale_order(self):
        return {
            'name':'Sales',
            'view_mode':'tree,form',
            'res_model':'sale.order',
            'type':'ir.actions.act_window',
            'domain': [('x_sheet_id', '=', self.id)],
            'target':'current',
            'context': {
                'search_default_x_sheet_id': self.id,
                'default_x_sheet_id': self.id},
        }

    def action_open_stock_move(self):
        picking_type_id = self.env['x_mjb_planning_sheet_opt'].search([('x_code', '=', 'RESUPPLY_OPERATION_TYPE_ID'), ('x_company_id', '=', self.x_company_id.id)])
        return {
            'name':'Resupply',
            'view_mode':'tree,form',
            'res_model':'stock.picking',
            'type':'ir.actions.act_window',
            'domain': [('x_sheet_id', '=', self.id), ('picking_type_id', '=', int(picking_type_id.x_name))],
            'target':'current',
            'context': {
                'search_default_x_sheet_id': self.id,
                'default_x_sheet_id': self.id},
        }








