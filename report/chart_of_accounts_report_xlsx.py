
from datetime import datetime
import time

# from numpy import product
from odoo import api, models
from dateutil.parser import parse
from odoo.exceptions import UserError

class ChartOfAccountsReportXlsx(models.AbstractModel):
    _name = "report.chart_of_accounts_report.chart_of_accounts_xlsx"
    _inherit = 'report.report_xlsx.abstract'
    _description = "Chart Of Accounts Xlsx Report"

    @api.model
    def generate_xlsx_report(self, workbook, data, products):
    
        bold = workbook.add_format({'bold':True})
        sheet=workbook.add_worksheet('Chart Of Accounts Report')
        row = 0
        col = 0
                        
        sheet.write(row, col, 'Code', bold)

        col += 1
        sheet.write(row, col, 'Account Name', bold)

        col += 1
        sheet.write(row, col, 'Type', bold)

        col += 1
        sheet.write(row, col, 'Allow Reconcilliation', bold)

        # col += 1
        # sheet.write(row, col, 'Account Currency', bold) 

        for obj in data['products']:  
                       
            # if(data['start_date'][0]['start_date'] <= obj['create_date'] and data['end_date'][0]['end_date'] >= obj['create_date']):

            row += 1 
            
            sheet.write(row, col - 3, obj['code'])
            sheet.write(row, col - 2, obj['name'])
            sheet.write(row, col - 1, obj['user_type_id'][1])
            sheet.write(row, col, obj['reconcile'])
            # sheet.write(row, col, obj['currency_id'][1])
            
            # print("data date:", obj['currency_id'])


        