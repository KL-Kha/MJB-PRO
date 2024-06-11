# account_move.py
from odoo import models, api, _

class AccountMove(models.Model):
    _inherit = 'account.move'

    @api.constrains('ref', 'move_type', 'partner_id', 'journal_id', 'invoice_date', 'state')
    def _check_duplicate_supplier_reference(self):
        """ Override to disable the RedirectWarning on duplicate supplier references """
        disable_vendor_ref_warning = self.env['ir.config_parameter'].sudo().get_param(
            'mjb_disable_vendor_ref_warning.disable_vendor_ref_warning', False
        )
        if disable_vendor_ref_warning:
            pass
        else:
            res = super(AccountMove,self)._check_duplicate_supplier_reference()
            return res