{
    "name": "Planning Sheet Base",
    "author": "Majorbird",
    "version": "16.0.0.0.1",
    "category": "Hidden",
    "summary": "This module includes several crucial features that help users to plan effectively. This module can improve the entire planning process, offering benefits such as increased visibility, flexibility and control over manufacturing and sales progression.",
    "website": "majorbird.cn",
    "depends": [
        "base",
        "mail",
        "purchase",
        "sale",
        "sale_management",
        "mrp",
        "base_automation",
    ],
    "data": [
        'security/ir.model.access.csv',
        'data/ir_sequence_data.xml',
        'data/automated_action_data.xml',
        'data/server_action_data.xml',
        'data/x_mjb_planning_sheet_stage_data.xml',
        'data/x_mjb_planning_sheet_opt_data.xml',
        'wizard/x_mjb_planning_wizard_views.xml',
        'views/x_mjb_planning_sheet_line_views.xml',
        'views/x_mjb_planning_sheet_opt_views.xml',
        'views/x_mjb_planning_sheet_stage_views.xml',
        'views/x_mjb_planning_sheet_views.xml',
        'views/product_views.xml',
        'views/product_template_views.xml',
    ],
    "_documentation": {
        "banner": "banner.jpg",
        "icon": "icon.png",
        "excerpt": "The Odoo MRP system plans routes from top to bottom, which means that the planning team doesn't see full requirements for a certain order until they actually plan it.",
        "summary": "Our module introduces a new approach to using Manufacturing Resource Planning (MRP) in Odoo, known as 'Planning Sheet'. This module includes several crucial features that help users to plan effectively. Team can select the order or products they want to plan for and compute the MRP. The plan is validated through a process. The module can generate Purchase or Manufacturing Orders for chosen products which can assist in tracking the correlation. The Planning Sheet module can improve the entire planning process, offering benefits such as increased visibility, flexibility and control over manufacturing and sales progression.",
        "issue": " In many cases, users want to compute everything first, then make decisions. Not just let the MRP compute steps one by one as each Manufacturing Order, Purchase Order, or picking process is confirmed.",
        "solution": "This module introduces a new way to use MRP in Odoo, known as the 'Planning Sheet'. This strategy closely mirrors the standard Odoo MRP features, but adds flexibility in defining requirements and simulating results.",
        
        "manual": [
            {
                "title": "Installation",
                "description": "Find the module in the app list and click install!",
                "images": ["image1.png"],
            },
            {
                "title": "Go to Planning Sheet",
                "description": "Ensure you have access rights to the Planning Sheet, then navigate to the Planning Sheet menu",
                "images": ["image2.png"],
            },
            {
                "title": "Trigger the MRP computation",
                "description": "Follow the given instructions. If you wish, you can also trigger the MRP computation.",
                "images": ["image3.png"],
            },
            {
                "title": "Make the decision for the quantity",
                "description": "Follow the given instructions. You have the choice to set the quantity to actually plan.",
                "images": ["image4.png"],
            },
            {
                "title": "Place Purchase Order, Manufacturing Order, subcontracted Purchase Order",
                "description": "Follow the given instructions. All Purchase Orders, Manufacturing Orders, and subcontracted Purchase Orders will be tied to the planning sheet to keep track of their correlation.",
                "images": ["image5.png"],
            },
        ],

        "features": [
            {
                "title": "Add Order",
                "description": "Pick the orders you want to include in your planning!"
            },
            {
                "title": "Add Products",
                "description": "Select the products you want to include in your planning!"
            },
            {
                "title": "Compute",
                "description": "Start the MRP computation process."
            },
            {
                "title": "Confirm",
                "description": "Your planning is confirmed (through a validation process)!"
            },
            {
                "title": "Buy",
                "description": "This will create Purchase Orders for the selected lines under the 'Buy' tab, and include them in the 'Planned Purchase Lines'!"
            },
            {
                "title": "Subcontract",
                "description": "This will create Purchase Orders for the selected lines under the 'Subcontract' tab, and include them in the 'Planned Purchase Lines'!"
            },
            {
                "title": "Manufacture",
                "description": "This will create Manufacturing Orders for the selected lines under the 'Manufacture' tab, and include them in the 'Planned Manufacturing Orders'!"
            },
            {
                "title": "Close",
                "description": "This will move the planning sheet to a closed state!"
            },
            {
                "title": "Back",
                "description": "This will revert planning sheet to its previous state!"
            },
        ],
    },
    "license": "OPL-1",
    "installable": True,
    "images": [],
}
