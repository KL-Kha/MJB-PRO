from odoo import fields, models, _
from odoo.exceptions import UserError


class mjb_journal_entry_report_wizard(models.TransientModel):
    _name = "mjb.journal.entry.report.wizard"
    _description = 'Journal Entries Report Wizard'

    start_date = fields.Date(string='Start Date', required=1)
    end_date = fields.Date(string='End Date', required=1)

    def action_print(self):
        self.ensure_one()
        account_move_obj = self.env['account.move']
        if self.end_date < self.start_date:
            raise UserError(_("Start date cannot be greater then end date!"))
        account_move_ids = account_move_obj.search([
            ('date', '>=', self.start_date),
            ('date', '<=', self.end_date)])
        if account_move_ids:
            return self.env.ref(
                'mjb_l10n_cn_report.mjb_action_journal_entry_report'
            ).report_action(account_move_ids)
        else:
            raise UserError(_('No Journal Entries Found'))

# end of validate_sales_forecast_history_wizard()
