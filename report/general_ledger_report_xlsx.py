
from datetime import datetime
import time

# from numpy import product
from odoo import api, models
from dateutil.parser import parse
from odoo.exceptions import UserError

class GeneralLedgerReportXlsx(models.AbstractModel):
    _name = "report.general_ledger_report.general_ledger_xlsx"
    _inherit = 'report.report_xlsx.abstract'
    _description = "Chart Of Accounts Xlsx Report"

    @api.model
    def generate_xlsx_report(self, workbook, data, products):
    
        bold = workbook.add_format({'bold':True})
        sheet=workbook.add_worksheet('General Ledger Report')
        row = 0
        col = 0
                        
        sheet.write(row, col, 'Date', bold)

        col += 1
        sheet.write(row, col, 'Journal Entry', bold)

        col += 1
        sheet.write(row, col, 'Product', bold)

        col += 1
        sheet.write(row, col, 'Amount In Currency', bold)

        col += 1
        sheet.write(row, col, 'Debit', bold)

        col += 1
        sheet.write(row, col, 'Credit', bold)

        col += 1
        sheet.write(row, col, 'Balance', bold)

        col += 1
        sheet.write(row, col, 'Cumulated Balance', bold)

        col += 1
        sheet.write(row, col, 'Matching', bold)

        # col += 1
        # sheet.write(row, col, 'Account Currency', bold) 

        for obj in data['products']:  
                       
            # if(data['start_date'][0]['start_date'] <= obj['date'] and data['end_date'][0]['end_date'] >= obj['date']):

            row += 1 
            
            sheet.write(row, col - 8, obj['date'])
            sheet.write(row, col - 7, obj['move_id'][1])
            sheet.write(row, col - 6, obj['name'])
            sheet.write(row, col - 5, obj['amount_currency'])
            sheet.write(row, col - 4, obj['debit'])
            sheet.write(row, col - 3, obj['credit'])
            sheet.write(row, col - 2, obj['balance'])
            sheet.write(row, col - 1, obj['cumulated_balance'])
            sheet.write(row, col, obj['matching_number'])
            
            # print("data date:", data)


        