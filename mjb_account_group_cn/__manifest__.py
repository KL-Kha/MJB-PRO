# -*- coding: utf-8 -*-
{
    "name": "Account Groups - Chinese",
    "version": "16.0.1.0.0",
    'license': 'OPL-1',
    'summary': 'Libraries of account groups',
    'category': 'Localization',
    'author': "Majorbird",
    'website': "https://www.odoo.com",
    'support': 'odoo@majorbird.cn',
    "description": """
        Account Groups Chinese

        Add libraries of account groups chinese
    """,
    "depends": [
        'account',
        'mjb_l10n_cn',
    ],
    'data': [
        'data/l10n_cn_groups.xml',
        'data/account_account_template.xml',
    ],
    'images': [
        'static/description/account_groups_cn_screenshot.png'
    ],
    'demo': [
    ],
    'application': False,
    'post_init_hook': 'post_init_hook',
}
