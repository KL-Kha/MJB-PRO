from odoo import api, fields, models, _
from odoo.exceptions import ValidationError, UserError

class XMjbPlanningSheetLine(models.Model):
    _inherit = "x_mjb_planning_sheet_line"

    x_bom_ids = fields.Many2many('mrp.bom', string="BOM IDs")
    x_bom_type = fields.Char(string="BOM type")
    x_parent_bom_id = fields.Many2one('mrp.bom', string="Parent BOM")
    x_purchased_qty = fields.Float(string="Purchased Qty")
    x_supplier_ids = fields.Many2many('res.partner', string="Supplier IDs")
    x_unit_price = fields.Float(string="Unit Price", digits=(12,4))

    def _default_x_defect_rate(self):
        for record in self:
            try:
                PRODUCT_DEFECT_RATE_CATEGORY_ID = record.env.ref('x_mjb_planning_sheet_pro_ext.x_mjb_planning_sheet_product_categ_rate').x_name or []
                if len(PRODUCT_DEFECT_RATE_CATEGORY_ID) > 1:
                    PRODUCT_DEFECT_RATE_CATEGORY_ID = PRODUCT_DEFECT_RATE_CATEGORY_ID.split(',')
                INT_PRODUCT_DEFECT_RATE_CATEGORY_ID = [int(item.strip()) for item in PRODUCT_DEFECT_RATE_CATEGORY_ID]
            except:
                raise ValidationError(_('Unacceptable for the PRODUCT_DEFECT_RATE_CATEGORY_ID'))

            try:
                DEFECT_RATE_FOR_PRODUCT_CATEGORY = record.env.ref('x_mjb_planning_sheet_pro_ext.x_mjb_planning_sheet_x_defect_rate').x_name or 0.0
                DEFECT_RATE_FOR_PRODUCT_CATEGORY = float(DEFECT_RATE_FOR_PRODUCT_CATEGORY)
            except:
                raise ValidationError(_('Unacceptable for the DEFECT_RATE_FOR_PRODUCT_CATEGORY'))

            if record.x_product_id.categ_id and record.x_product_id.categ_id.id in INT_PRODUCT_DEFECT_RATE_CATEGORY_ID:
                return DEFECT_RATE_FOR_PRODUCT_CATEGORY
            else:
                return 0

    x_defect_rate = fields.Float(string="Defect Rate", default=_default_x_defect_rate)