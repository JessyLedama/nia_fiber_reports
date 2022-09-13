
from pickle import FALSE
import time

# from numpy import product

from numpy import product
from odoo import api, models
from dateutil.parser import parse
from odoo.exceptions import UserError

class ProductInvoiceXlsx(models.AbstractModel):
    _name = "report.inventory_aging_report.inventory_aging_report_xlsx"
    _inherit = 'report.report_xlsx.abstract'
    _description = "Inventory Aging Report"

    @api.model
    def generate_xlsx_report(self, workbook, data, products):
    
        period = data['form_data']['period']
        increment = data['form_data']['period']
        limit = data['form_data']['limit']
        
        bold = workbook.add_format({'bold':True})
        sheet=workbook.add_worksheet('Inventory Aging Report')
        row = 0
        col = 0
                        
        sheet.write(row, col, 'Product Name', bold)

        col += 1
        sheet.write(row, col, 'Total Qty', bold)

        col += 1
        sheet.write(row, col, 'Total Value', bold)

        col += 1
        sheet.write(row, col, 'Currency', bold)

        while period <= limit:
            col += 1
            sheet.write(row, col, period, bold)

            period = period + increment


    
        for obj in data['products']: 
            totalValue = obj['price_unit']*obj['quantity'] 

            row += 1  
            
            if(obj['product_id'] != False):
                if(data['form_data']['start_date'] <= obj['date']):
                    sheet.write(row, col - 8, obj['product_id'][1])
                    sheet.write(row, col - 7, obj['quantity'])
                    sheet.write(row, col - 6, totalValue)
                    sheet.write(row, col - 5, obj['currency_id'][1])
                    
                    print("data date:", obj['product_id'])


        