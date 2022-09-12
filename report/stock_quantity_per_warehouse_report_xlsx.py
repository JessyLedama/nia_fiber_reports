
from datetime import datetime
import time

# from numpy import product
from odoo import api, models
from dateutil.parser import parse
from odoo.exceptions import UserError

class StockQtyPerWhouseReportXlsx(models.AbstractModel):
    _name = "report.stock_qty_per_whouse_report.stock_qty_per_whouse_xlsx"
    _inherit = 'report.report_xlsx.abstract'
    _description = "Stock Quantity Per Warehouse Xlsx Report"

    @api.model
    def generate_xlsx_report(self, workbook, data, products):
    
        bold = workbook.add_format({'bold':True})
        sheet=workbook.add_worksheet('Stock Quantity Per Warehouse Report')
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
        sheet.write(row, col, 'Units Of Measure', bold)   

        col += 1
        sheet.write(row, col, 'Total Cost', bold) 

        col += 1
        sheet.write(row, col, 'Total Sales Price', bold) 

        for obj in data['products']:  
                       
            if(obj['quantity'] >= 0):

                if(data['location'][0]['warehouse_id'][0] == obj['location_id'][0]):

                    product = self.env['product.product'].search_read([('id', '=', obj['product_id'][0])])

                    totalCost = product[0]['standard_price'] * obj['quantity']
                    totalPrice = product[0]['list_price'] * obj['quantity']

                    row += 1 
                    
                    sheet.write(row, col - 7, obj['product_id'][1])
                    sheet.write(row, col - 6, product[0]['list_price'])
                    sheet.write(row, col - 5, product[0]['standard_price'])
                    sheet.write(row, col - 4, product[0]['currency_id'][1])
                    sheet.write(row, col - 3, obj['quantity'])
                    sheet.write(row, col - 2, obj['product_uom_id'][1])
                    sheet.write(row, col - 1, totalCost)
                    sheet.write(row, col , totalPrice)
                    
                    # print("data date:", product[0]['list_price'])


        