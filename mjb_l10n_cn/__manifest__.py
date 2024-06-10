# -*- coding: utf-8 -*-
# Part of Odoo Majorbird Edition.
# See LICENSE file for full copyright and licensing details.
{
    'name': 'China - Accounting',
    'version': '16.0.1.0.0',
    'license': 'OPL-1',
    'author': 'Majorbird',
    'website': "https://www.odoo.com",
    'category': 'Localization',
    'summary': 'Manage the accounting chart (with hierarchy) for China',
    'support': 'odoo@majorbird.cn',
    'description': """
This is the module to manage
the accounting chart (with hierarchy) for China in Odoo.
(China COA)
""",
    'depends': [
        'base',
        'account',
    ],
    'data': [
        'data/account_chart_type.xml',
        'data/account_chart_general_business_template.xml',
        'data/account_tax_template.xml',
        'data/account_chart_post_data.xml',
        'views/account_chart_type_views.xml',
    ],

    'demo': [
    ],
    'price': 360.00,
    'currency': 'EUR',
    'application': False,
}
