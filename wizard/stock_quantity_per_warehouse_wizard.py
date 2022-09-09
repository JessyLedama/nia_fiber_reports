# -*- coding: utf-8 -*-
#################################################################################
#
#    Odoo, Open Source Management Solution
#    Copyright (C) 2021-today Ascetic Business Solution <www.asceticbs.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#################################################################################

from email.policy import default
from pickle import TRUE

from sqlalchemy import true
from odoo import api, fields, models, _

class StockQuantityPerWarehouseReport(models.TransientModel):
    _name = "stock.quantity.per.warehouse.report"
    _description = "Stock Quantity Per Warehouse Report"

    warehouse_id = fields.Many2one('stock.location', string="Warehouse")
    total_amount_due = fields.Integer(string='Total Amount Due')


    #PDF Report
    # def check_report(self):
    #     data = {}
    #     data['form'] = self.read(['start_date', 'end_date'])[0]
    #     return self._print_report(data)

    # def _print_report(self, data):
    #     data['form'].update(self.read(['start_date', 'end_date'])[0])
    #     return self.env.ref('nia_fiber_reports.action_product_invoice').report_action(self, data=data, config=False)


    # Excel Report
    def check_excel_report(self):
        warehouseId = self.read(['warehouse_id'])[0]
        products = self.env['stock.quant'].search_read([('location_id', '=', 8)]) 

        data = {
            'location': warehouseId,
            'products': products,
        }

        return self.print_excel_report(data,)

    def print_excel_report(self, data):
        return self.env.ref('nia_fiber_reports.action_stock_quantity_per_warehouse_report_xlsx').report_action(self, data=data, config=False)
        