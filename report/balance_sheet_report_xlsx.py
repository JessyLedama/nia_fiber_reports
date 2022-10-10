
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
                        
        sheet.write(row, col, 'Name', bold)

        col += 1
        sheet.write(row, col, 'Debit', bold)

        col += 1
        sheet.write(row, col, 'Credit', bold)

        col += 1
        sheet.write(row, col, 'Balance', bold) 

        for obj in data['products']:  
                       
            name = self.env['financial.report'].search_read([('create_date', '>=', startDate['start_date']), ('create_date', '<=', endDate['end_date'])]) 
            # if(data['start_date'][0]['start_date'] <= obj['create_date'] and data['end_date'][0]['end_date'] >= obj['create_date']):
            
            row += 1 
            
            # sheet.write(row, col - 6, obj['name'][1])
            # sheet.write(row, col - 5, obj['product_id'][1])
            # sheet.write(row, col - 4, obj['quantity'])
            # sheet.write(row, col - 3, obj['product_uom_id'][1])
            # sheet.write(row, col - 2, obj['inventory_quantity'])
            # sheet.write(row, col - 1, obj['inventory_diff_quantity'])
            sheet.write(row, col, obj['id'])
            
            print("data date:", data['target_moves']['target_moves'])


        