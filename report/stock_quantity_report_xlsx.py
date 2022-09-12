
from datetime import datetime
import time

# from numpy import product
from odoo import api, models
from dateutil.parser import parse
from odoo.exceptions import UserError

class StockQuantityReportXlsx(models.AbstractModel):
    _name = "report.stock_quantity_report.stock_quantity_xlsx"
    _inherit = 'report.report_xlsx.abstract'
    _description = "Stock Quantity Xlsx Report"

    @api.model
    def generate_xlsx_report(self, workbook, data, products):
    
        bold = workbook.add_format({'bold':True})
        sheet=workbook.add_worksheet('Stock Quantity Report')
        row = 0
        col = 0
                        
        sheet.write(row, col, 'Product Name', bold)

        col += 1
        sheet.write(row, col, 'Sales Price', bold)

        col += 1
        sheet.write(row, col, 'Cost', bold)

        col += 1
        sheet.write(row, col, 'Currency', bold)

        col += 1
        sheet.write(row, col, 'Quantity On Hand', bold)

        col += 1
        sheet.write(row, col, 'Forecasted Quantity', bold) 

        col += 1
        sheet.write(row, col, 'Units Of Measure', bold)   

        col += 1
        sheet.write(row, col, 'Total Cost', bold) 

        col += 1
        sheet.write(row, col, 'Total Price', bold) 

        for obj in data['products']:  
                       
            # if(data['start_date'][0]['start_date'] <= obj['create_date'] and data['end_date'][0]['end_date'] >= obj['create_date']):

            totalCost = obj['standard_price'] * obj['qty_available']
            totalPrice = obj['list_price'] * obj['qty_available']

            row += 1 
            
            sheet.write(row, col - 8, obj['name'])
            sheet.write(row, col - 7, obj['list_price'])
            sheet.write(row, col - 6, obj['standard_price'])
            sheet.write(row, col - 5, obj['currency_id'][1])
            sheet.write(row, col - 4, obj['qty_available'])
            sheet.write(row, col - 3, obj['virtual_available'])
            sheet.write(row, col - 2, obj['uom_id'][1])
            sheet.write(row, col - 1, totalCost)
            sheet.write(row, col , totalPrice)
            
            # print("data date:", obj['order_id'])


        