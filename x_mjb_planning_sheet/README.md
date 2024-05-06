# Planning Sheet Base 

The Odoo MRP system plans routes from top to bottom, which means that the planning team doesn't see full requirements for a certain order until they actually plan it.

**Before** 

 In many cases, users want to compute everything first, then make decisions. Not just let the MRP compute steps one by one as each Manufacturing Order, Purchase Order, or picking process is confirmed.

**After**
 
This module introduces a new way to use MRP in Odoo, known as the 'Planning Sheet'. This strategy closely mirrors the standard Odoo MRP features, but adds flexibility in defining requirements and simulating results.

## Manual

### Installation
Find the module in the app list and click install!

![image1](https://gitlab.com/mjb.customers/out/enroutebizz//raw/16.0/x_mjb_planning_sheet/static/description/image1.png?inline=false)
 
### Go to Planning Sheet
Ensure you have access rights to the Planning Sheet, then navigate to the Planning Sheet menu

![image2](https://gitlab.com/mjb.customers/out/enroutebizz//raw/16.0/x_mjb_planning_sheet/static/description/image2.png?inline=false)
 
### Trigger the MRP computation
Follow the given instructions. If you wish, you can also trigger the MRP computation.

![image3](https://gitlab.com/mjb.customers/out/enroutebizz//raw/16.0/x_mjb_planning_sheet/static/description/image3.png?inline=false)
 
### Make the decision for the quantity
Follow the given instructions. You have the choice to set the quantity to actually plan.

![image4](https://gitlab.com/mjb.customers/out/enroutebizz//raw/16.0/x_mjb_planning_sheet/static/description/image4.png?inline=false)
 
### Place Purchase Order, Manufacturing Order, subcontracted Purchase Order
Follow the given instructions. All Purchase Orders, Manufacturing Orders, and subcontracted Purchase Orders will be tied to the planning sheet to keep track of their correlation.

![image5](https://gitlab.com/mjb.customers/out/enroutebizz//raw/16.0/x_mjb_planning_sheet/static/description/image5.png?inline=false)
  
## Features

#### Add Order
Pick the orders you want to include in your planning!

#### Add Products
Select the products you want to include in your planning!

#### Compute
Start the MRP computation process.

#### Confirm
Your planning is confirmed (through a validation process)!

#### Buy
This will create Purchase Orders for the selected lines under the 'Buy' tab, and include them in the 'Planned Purchase Lines'!

#### Subcontract
This will create Purchase Orders for the selected lines under the 'Subcontract' tab, and include them in the 'Planned Purchase Lines'!

#### Manufacture
This will create Manufacturing Orders for the selected lines under the 'Manufacture' tab, and include them in the 'Planned Manufacturing Orders'!

#### Close
This will move the planning sheet to a closed state!

#### Back
This will revert planning sheet to its previous state!

## About Majorbird
Majorbird is a leading software engineering and consulting firm based in Shenzhen, Guangdong, China. As an official Odoo Silver Partner, we have a proven track record of successfully implementing Odoo in over 30 projects. We understand the importance of ERP systems in today's business world and our goal is to support our customers closely to ensure success in their ERP projects.

[Contact us](https://majorbird.cn/contactus)

![Majorbird logo](https://gitlab.com/mjb.customers/out/enroutebizz//raw/16.0/x_mjb_planning_sheet/static/description/logo.png?inline=false)
![Silver logo](https://gitlab.com/mjb.customers/out/enroutebizz//raw/16.0/x_mjb_planning_sheet/static/description/logo_silver.png?inline=false) 

### Majorbird Vietnam Office
Tower SAV1, The Sun Avenue Apartment, Hochiminh, Vietnam

[https://majorbird.vn/](https://majorbird.vn/)

[odoo@majorbird.cn](mailto:odoo@majorbird.cn?subject=VN%20MODULE%20Planning%20Sheet%20Base)

### Majorbird China Office 
深圳市南山区招商街道沿山社区南海大道1079号花园城数码大厦A座201, 518000, Shenzhen, China

[https://majorbird.cn/](https://majorbird.cn/)

[odoo@majorbird.cn](mailto:odoo@majorbird.cn?subject=CN%20MODULE%20Planning%20Sheet%20Base)
