{
    "name": "Accounting Stock Card",
    "author": "Majorbird",
    "version": "16.0.0.0.1",
    "category": "Accounting/Accounting",
    "summary": "Accounting Stock Card.",
    "website": "majorbird.cn",
    "depends": [
        'base',
        'account',
        'account_accountant',
        'account_reports',
        'stock',
        'purchase',
    ],
    "data": [
        'data/server_action_data.xml',
        'security/ir.model.access.csv',
        'views/x_mjb_stock_card_views.xml',
        'views/x_mjb_stock_card_line_views.xml',
    ],
    "license": "OPL-1",
    "installable": True,
    "images": [],
}
