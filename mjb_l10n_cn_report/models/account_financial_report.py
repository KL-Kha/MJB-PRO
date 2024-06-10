from odoo import fields, models, api, _
from datetime import datetime


class AccountReportLine(models.Model):
    _inherit = "account.report.line"

    # mjb_is_page2 = fields.Boolean('Page 2')
    period = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # def get_lines(self, financial_report, currency_table, options, linesDicts):
    #     res = super(AccountReportLine, self).get_lines(
    #         financial_report, options, currency_table, linesDicts)
    #     for line in self:
    #         report_lines = filter(lambda x: x['id'] == line.id, res)
    #         # print report_lines
    #         for report_line in report_lines:
    #             report_line['mjb_is_page2'] = line.mjb_is_page2
    #     return res

# end of AccountReportLine()

class IrUiMenu(models.Model):
    _inherit = "ir.ui.menu"

    @api.model
    def create(self, vals):
        if vals.get('name') == 'China Profit & Loss':
            vals.update({
                'sequence': 1
            })
        if vals.get('name') == 'China Balance Sheet':
            vals.update({
                'sequence': 4
            })
        if vals.get('name') == 'China Legal Profit & Loss':
            vals.update({
                'sequence': 7
            })

        return super(IrUiMenu, self).create(vals)
