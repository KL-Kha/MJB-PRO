{
    "name": "Planning Sheet Pro",
    "author": "Majorbird",
    "version": "16.0.0.0.1",
    "category": "Hidden",
    "summary": "This module is designed to refine the planning process in Odoo by offering a more comprehensive, end-to-end planning solution.",
    "website": "majorbird.cn",
    "depends": [
        "base",
        "mail",
        "purchase",
        "sale",
        "sale_management",
        "mrp",
        "base_automation",
        "x_mjb_planning_sheet",
    ],
    "data": [
        'security/ir.model.access.csv',
        'data/automated_action_data.xml',
        'data/server_action_data.xml',
        'data/x_mjb_planning_sheet_opt_data.xml',
        'wizard/x_mjb_planning_wizard_views.xml',
        'views/mrp_bom_views.xml',
        'views/x_mjb_planning_sheet_views.xml',
        'views/x_mjb_planning_sheet_line_views.xml',
        'views/sale_order_line_views.xml',
    ],
    "assets": {
        "web.assets_backend": [
            "x_mjb_planning_sheet_pro_ext/static/src/scss/style.scss",
        ],
    },
    "license": "OPL-1",
    "_documentation": {
        "banner": "banner.jpg",
        "icon": "icon.png",
        "excerpt": "The standard functionality of Odoo's MRP operates in a top-down fashion, planning routes and triggering them. This means that the planning team does not have a full visibility of the requirements for a particular order until it is actually planned.",  
        "summary": "The Planning Sheet Pro Module is designed to refine the planning process in Odoo by offering a more comprehensive, end-to-end planning solution. It allows users to compute their entire requirement first, after which decisions can be made. Instead of letting the MRP compute step-by-step each time a purchase order, sale order, or picking is confirmed, users can utilise the 'Planning Sheet' function to follow close to standard features of Odoo's MRP while also availing flexible definition of needs and simulation capabilities. The variation also introduces several advanced features in the planning process such as planning for orders or products, triggering MRP computation, confirming plans, generating various orders, reverting changes and closing orders.",  
        "issue": "Users often want to compute the entire requirement before making decisions, rather than letting the MRP step-by-step compute each time a Manufacturing Order, Purchase Order, or picking is confirmed.",  
        "solution": "This issue is addressed by using a new approach called 'Planning Sheet'. This new function works closely with standard features in Odoo MRP, offering more flexibility in defining needs and simulation capabilities.",  
        "manual": [  
            {  
            "title": "Installation",  
            "description": "Look for the module in the app list and install with a single click",  
            "images": ["image1.png"]  
            },  
            {  
            "title": "Navigating to Planning Sheet",  
            "description": "Once you have the necessary access rights, head over to the Planning Sheet menu",  
            "images": ["image2.png"]  
            },  
            {  
            "title": "Triggering MRP computation",  
            "description": "Follow the instructions. Alternatively, if you wish, the system allows you to run MRP computation",  
            "images": ["image3.png"]  
            },  
            {  
            "title": "Specification of quantity",  
            "description": "Follow the instructions and specify the quantity to plan. The system provides you with the flexibility for actual planning",  
            "images": ["image4.png"]  
            },  
            {  
            "title": "Creation of various orders",  
            "description": "Following the instructions, Purchase Orders, Manufacturing Orders, subcontracted Purchase Orders, Sale Orders, and Resupply Orders will attach to the Planning Sheet for record-keeping",  
            "images": ["image5.png"]  
            }  
        ],
        "features": [  
            {  
            "title": "Add Order",  
            "description": "Gives you the flexibility to plan for the orders you want!"  
            },  
            {  
            "title": "Add Products",  
            "description": "Provides the capability to plan for any products you select!"  
            },  
            {  
            "title": "Compute",  
            "description": "MRP computation can be triggered anytime."  
            },  
            {  
            "title": "Confirm",  
            "description": "You can confirm the plan through a validation process"  
            },  
            {  
            "title": "Buy",  
            "description": "Generate Purchase Orders from selected lines in the 'Buy' tab."  
            },  
            {  
            "title": "Subcontract",  
            "description":  "Generates Purchase Orders for selected lines under the 'Subcontract' tab."  
            },  
            {  
            "title": "Manufacture",  
            "description": "Generates Manufacturing Orders for selected lines in the 'Manufacture' tab."  
            },  
            {  
            "title": "Sell",  
            "description": "Generates Sale Orders for selected lines in the 'Buy' tab."  
            },  
            {  
            "title": "Resupply",  
            "description": "Generates supply order(s) for selected lines in the 'Kit' tab."  
            },  
            {  
            "title": "Close",  
            "description": "Allows you to move the planning sheet to a closed state"  
            },  
            {  
            "title": "Back",  
            "description": "Lets you revert the planning sheet to the previous state"  
            }  
        ],  
    },
    "installable": True,
    "images": [],
}
