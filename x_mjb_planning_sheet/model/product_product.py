from odoo import api, fields, models


class ProductProduct(models.Model):
    _inherit = "product.product"

    x_qty_internal_location = fields.Float(
        'Quantity Internal Location', compute='_compute_x_qty_internal_location',
        digits='Product Unit of Measure',
        help="Current quantity of products in internal location.\n"
             "In a context with a single Stock Location, this includes "
             "goods stored at this Location, or any of its children.\n"
             "In a context with a single Warehouse, this includes "
             "goods stored in the Stock Location of this Warehouse, or any "
             "of its children.\n"
             "stored in the Stock Location of the Warehouse of this Shop, "
             "or any of its children.\n"
             "Otherwise, this includes goods stored in any Stock Location "
             "with 'internal' type.")
    
    def _compute_x_qty_internal_location(self):
        for rec in self:
            quants = self.env['stock.quant'].read_group([('location_id.usage', '=', 'internal'), ('product_id', '=', self.id)], ['product_id', 'quantity'], ['product_id'], orderby='id')
            if quants:
                rec.x_qty_internal_location = quants[0]['quantity']
            else:
                rec.x_qty_internal_location = 0.0

    def action_open_quants_internal_location(self):
        return {
            'name':'Quantity Internal Location',
            'view_mode':'tree',
            'res_model':'stock.quant',
            'type':'ir.actions.act_window',
            'domain': [('product_id', '=', self.id)],
            'target':'current',
            'context': {
                'search_default_internal_loc': 1,
                'search_default_locationgroup': 1,
            },
        }