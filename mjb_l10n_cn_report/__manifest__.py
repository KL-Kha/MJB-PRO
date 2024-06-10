# -*- coding: utf-8 -*-
# Part of Odoo Majorbird Edition.
# See LICENSE file for full copyright and licensing details.
{
    "name": "ACC: Majorbird China Report",
    'version': '16.0.1.0.0',
    'license': 'OPL-1',
    'author': "Majorbird",
    'sequence': 15,
    'category': 'Reporting',
    'website': "https://www.odoo.com",
    'support': 'odoo@majorbird.cn',
    "description": """
    Module to developed Majorbird China reporting.
    """,
    "depends": ['base', 'account', 'mjb_l10n_cn', 'account_reports', 'mjb_account_group_cn'],
    'init_xml': [],
    'data': [
        'security/ir.model.access.csv',
        # 'data/account_financial_report_data.xml',
        'data/china_legal_profit_and_loss.xml',
        'data/china_legal_balance_sheet.xml',
        'data/menuitems.xml',
        'views/account_financial_report_template.xml',
        'wizard/mjb_journal_entry_report_wizard_view.xml',
        # 'views/account_financial_report_view.xml',
    ],
    'css': [],
    'js': [
    ],
    'qweb': [],
    'installable': True,
    'active': False,
    'price': 360.00,
    'currency': 'EUR',
    'application': False,
}
