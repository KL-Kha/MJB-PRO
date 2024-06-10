    # -*- coding: utf-8 -*-
{
    "name": "China Localization BS/PL",
    "version": "16.0.1.0.0",
    'license': 'OPL-1',
    'summary': 'Profit and loss for China',
    'category': 'Accounting and Finance',
    'website': "https://www.odoo.com",
    'support': 'odoo@majorbird.cn',
    "description": """
        Profit and loss for China
    """,
    "depends": [
        'account_reports',
        'mjb_l10n_cn',
        'mjb_account_group_cn',
        'mjb_l10n_cn_report',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/china_profit_and_loss.xml',
        'data/china_balance_sheet.xml',
        'data/menuitems.xml',
        'data/base_data_bs.xml',
        'data/base_data_pl.xml',
        'data/account_chart_general_business_template.xml',
        # 'data/report_pl_cn.xml',
        # 'data/financial_report_cn.xml',
        'views/account_views.xml',
    ],
    'images': [

    ],
    'post_init_hook': 'post_init_hook',
    'application': False,
}
