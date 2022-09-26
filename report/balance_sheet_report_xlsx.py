
from datetime import datetime
import time

# from numpy import product
from odoo import api, models
from dateutil.parser import parse
from odoo.exceptions import UserError

class BalanceSheetReportXlsx(models.AbstractModel):
    _name = "report.balance_sheet_report.balance_sheet_xlsx"
    _inherit = 'report.report_xlsx.abstract'
    _description = "Balance Sheet Xlsx Report"

    @api.model
    def generate_xlsx_report(self, workbook, data, products):
    
        bold = workbook.add_format({'bold':True})
        sheet=workbook.add_worksheet('Balance Sheet Report')
        row = 0
        col = 0
                        
        sheet.write(row, col, 'Location', bold)

        col += 1
        sheet.write(row, col, 'Product', bold)

        col += 1
        sheet.write(row, col, 'On Hand Quantity', bold)

        col += 1
        sheet.write(row, col, 'Unit Of Measure', bold) 

        col += 1
        sheet.write(row, col, 'Counted Quantity', bold)   

        col += 1
        sheet.write(row, col, 'Difference', bold)   

        col += 1
        sheet.write(row, col, 'Date', bold)

        for obj in data['products']:  
                       
            # if(data['start_date'][0]['start_date'] <= obj['create_date'] and data['end_date'][0]['end_date'] >= obj['create_date']):
            
            row += 1 
            
            # sheet.write(row, col - 6, obj['name'][1])
            # sheet.write(row, col - 5, obj['product_id'][1])
            # sheet.write(row, col - 4, obj['quantity'])
            # sheet.write(row, col - 3, obj['product_uom_id'][1])
            # sheet.write(row, col - 2, obj['inventory_quantity'])
            # sheet.write(row, col - 1, obj['inventory_diff_quantity'])
            # sheet.write(row, col, obj['create_date'])
            
            print("data date:", data['products'])


        