
import time

from odoo import api, models
from dateutil.parser import parse
from odoo.exceptions import UserError

class VendorBillsXlsx(models.AbstractModel):
    _name = "report.purchase_invoice_report.purchase_invoice_xlsx"
    _inherit = 'report.report_xlsx.abstract'
    _description = "Vendor Bills Xlsx Report"

    @api.model
    def generate_xlsx_report(self, workbook, data, products):
    
        bold = workbook.add_format({'bold':True})
        sheet=workbook.add_worksheet('Vendor Bills Report')
        row = 0
        col = 0
                        
        sheet.write(row, col, 'Vendor Bill', bold)

        col += 1
        sheet.write(row, col, 'Date', bold)

        col += 1
        sheet.write(row, col, 'Vendor', bold)

        col += 1
        sheet.write(row, col, 'Product', bold)

        col += 1
        sheet.write(row, col, 'Quantity', bold)

        col += 1
        sheet.write(row, col, 'Unit Of Measure', bold) 

        col += 1
        sheet.write(row, col, 'Unit Price', bold)   

        col += 1
        sheet.write(row, col, 'Amount', bold)

        col += 1
        sheet.write(row, col, 'Journal', bold)

    
        for obj in data['products']:  
            row += 1  
            
            if(data['form_data']['start_date'] <= obj['date'] and data['form_data']['end_date'] >= obj['date']):
                
                if(obj['price_unit'] >= 0):
                    sheet.write(row, col - 8, obj['move_id'][1])
                    sheet.write(row, col - 7, obj['date'])
                    sheet.write(row, col - 6, obj['partner_id'][1])
                    sheet.write(row, col - 5, obj['name'])
                    sheet.write(row, col - 4, obj['quantity'])
                    sheet.write(row, col - 2, obj['price_unit'])
                    sheet.write(row, col - 1, obj['price_total'])
                    sheet.write(row, col, obj['journal_id'][1])

                    # print("data date:", obj['journal_id'])


        