
from datetime import datetime
import time

# from numpy import product
from odoo import api, models
from dateutil.parser import parse
from odoo.exceptions import UserError

class StockAdjustmentReportXlsx(models.AbstractModel):
    _name = "report.stock_adjustment_report.stock_adjustment_xlsx"
    _inherit = 'report.report_xlsx.abstract'
    _description = "Stock Adjustment Xlsx Report"

    @api.model
    def generate_xlsx_report(self, workbook, data, products):
    
        bold = workbook.add_format({'bold':True})
        sheet=workbook.add_worksheet('Stock Adjustment Report')
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
            if(obj['quantity'] >= 0):
                if(obj['inventory_diff_quantity'] > 0):
                    locations = self.env['stock.location'].search_read([(('usage', 'not in', ['virual']))])

                    row += 1 
                    
                    sheet.write(row, col - 6, obj['location_id'][1])
                    sheet.write(row, col - 5, obj['product_id'][1])
                    sheet.write(row, col - 4, obj['quantity'])
                    sheet.write(row, col - 3, obj['product_uom_id'][1])
                    sheet.write(row, col - 2, obj['inventory_quantity'])
                    sheet.write(row, col - 1, obj['inventory_diff_quantity'])
                    sheet.write(row, col, obj['create_date'])
                    
                    # print("data date:", locations[0]['complete_name'])


        