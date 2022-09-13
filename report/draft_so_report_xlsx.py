
from datetime import datetime
import time

from numpy import product
from odoo import api, models
from dateutil.parser import parse
from odoo.exceptions import UserError

class DraftSOReportXlsx(models.AbstractModel):
    _name = "report.draft_so_report.draft_so_xlsx"
    _inherit = 'report.report_xlsx.abstract'
    _description = "Draft SO Xlsx Report"

    @api.model
    def generate_xlsx_report(self, workbook, data, products):
    
        bold = workbook.add_format({'bold':True})
        sheet=workbook.add_worksheet('Draft SO Report')
        row = 0
        col = 0
                        
        sheet.write(row, col, 'SO Number', bold)

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

        for obj in data['products']:  
                       
            if(data['start_date'][0]['start_date'] <= obj['create_date'] and data['end_date'][0]['end_date'] >= obj['create_date']):

                row += 1 
                
                sheet.write(row, col - 6, obj['order_id'][1])
                sheet.write(row, col - 5, obj['order_partner_id'][1])
                sheet.write(row, col - 4, obj['name'])
                sheet.write(row, col - 3, obj['product_uom_qty'])
                sheet.write(row, col - 2, obj['product_uom'][1])
                sheet.write(row, col - 1, obj['price_unit'])
                sheet.write(row, col, obj['price_total'])
                
                # print("data date:", obj['order_id'])


        