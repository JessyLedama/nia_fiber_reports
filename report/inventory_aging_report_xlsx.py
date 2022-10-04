
from pickle import FALSE
import time

# from numpy import product
from odoo import api, models
from dateutil.parser import parse
from odoo.exceptions import UserError
from datetime import date, datetime, timedelta

class AgingReportXlsx(models.AbstractModel):
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
                        
        sheet.write(row, col, 'Partner', bold)

        col += 1
        sheet.write(row, col, 'Account', bold)

        col += 1
        sheet.write(row, col, 'Number', bold)

        col += 1
        sheet.write(row, col, 'Currency', bold)
        
        col += 1
        sheet.write(row, col, 'Not Due', bold)

        while period <= limit:
            col += 1
            sheet.write(row, col, period, bold)

            period = period + increment


    
        for obj in data['products']: 
            
            dueDate = datetime.strptime(obj['invoice_date_due'],"%Y-%m-%d")
            startDate = datetime.strptime(data['form_data']['start_date'], "%Y-%m-%d")

            dateDiff = startDate - dueDate
            row += 1  
            
            sheet.write(row, col - 9, obj['invoice_partner_display_name'])
            sheet.write(row, col - 8, obj['journal_id'][1])
            sheet.write(row, col - 7, obj['name'])
            sheet.write(row, col - 6, obj['currency_id'][1])
            if(dateDiff.days <= 0):
                sheet.write(row, col - 5, obj['amount_total_signed'])
            elif(dateDiff.days <= 30):
                sheet.write(row, col - 4, obj['amount_total_signed'])
            elif(dateDiff.days <= 60 and dateDiff.days > 30):
                sheet.write(row, col - 3, obj['amount_total_signed'])
            elif(dateDiff.days <= 90 and dateDiff.days > 60):
                sheet.write(row, col -2, obj['amount_total_signed'])
            elif(dateDiff.days <= 120 and dateDiff.days > 90):
                sheet.write(row, col -1, obj['amount_total_signed'])
            elif(dateDiff.days <= 150 and dateDiff.days > 120):
                sheet.write(row, col, obj['amount_total_signed'])
    
            print("data date:", dateDiff.days)


        