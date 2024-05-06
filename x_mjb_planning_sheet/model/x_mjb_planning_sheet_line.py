from odoo import api, fields, models
import datetime


class XMjbPlanningSheetLine(models.Model):
    _name = "x_mjb_planning_sheet_line"
    _description = "Planning Sheet Line"
    _rec_name = "x_name"

    x_active = fields.Boolean(string="Active", default=True)
    x_available_quantity = fields.Float(string="Available Qty")
    x_bom_id = fields.Many2one('mrp.bom', string="BOM")
    x_buy_quantity = fields.Float(string="Buy Qty")
    x_code = fields.Char(string="Code")
    x_company_currency_id = fields.Many2one('res.currency', string="Currency Company")
    x_company_id = fields.Many2one('res.company', string="Company1")
    x_computed_quantity = fields.Float(string="Needed Qty")
    x_currency_id = fields.Many2one('res.currency', string="Currency")
    x_forecasted_quantity = fields.Float(string="Forecasted Qty")
    x_manufacture_quantity = fields.Float(string="Manufacture Qty")
    x_name = fields.Char(string="Name")
    x_notes = fields.Text(string="Notes")
    x_onhand_quantity = fields.Float(string="On Hand Qty")
    x_origin_line_ids = fields.One2many('x_mjb_planning_sheet_line', 'x_parent_line_id', string="Origins")
    x_parent_line_id = fields.Many2one('x_mjb_planning_sheet_line', string="Parent Line")
    x_product_id = fields.Many2one('product.product', string="Product")
    x_production_ids = fields.One2many('mrp.production', 'x_planner_sheet_line_id', string="Manufacturing Orders")
    x_purchase_order_line_ids = fields.One2many('purchase.order.line', 'x_sheet_line_id', string="Purchase Order Lines")
    x_quantity = fields.Float(string="Quantity")
    x_reserved_quantity = fields.Float(string="Reserved Qty")
    x_sale_order_line_id = fields.Many2one('sale.order.line', string="Sale Order Line")
    x_sequence = fields.Integer(string="Seq")
    x_sheet_id = fields.Many2one('x_mjb_planning_sheet', string="Sheet")
    x_subcontract_quantity = fields.Float(string="Subcontract Qty")
    x_supplier_id = fields.Many2one('res.partner', string="Supplier")
    x_total_price = fields.Float(string="Total Price", compute='_compute_total_price')
    x_total_price_signed = fields.Float(string="Total Price Signed", compute='_compute_total_price_signed')
    x_type = fields.Char(string="Type")
    x_unit_price = fields.Float(string="Unit Price")
    x_uom_id = fields.Many2one('uom.uom', string="UOM")

    @api.depends('x_quantity', 'x_unit_price')
    def _compute_total_price(self):
        for record in self:
            record.x_total_price = (record.x_unit_price or 0.0) * (record.x_quantity or 0.0)

    @api.depends('x_total_price', 'x_currency_id', 'x_company_currency_id', 'x_sheet_id.x_date')
    def _compute_total_price_signed(self):
        for record in self:
            rate = 1.0

            rDate = datetime.date.today()
            if record.x_sheet_id:
                if record.x_sheet_id.x_date:
                    rDate = record.x_sheet_id.x_date
            
            cRate = 1.0
            if record.x_currency_id:
                cRate = record.x_currency_id.with_context(date=rDate).rate or 1.0
            
            record.x_total_price_signed = (record.x_unit_price or 0.0) * (record.x_quantity or 0.0) / cRate
