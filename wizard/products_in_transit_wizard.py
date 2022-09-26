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
from odoo import api, fields, models, _

class ProductsInTransitReport(models.TransientModel):
    _name = "products.in.transit.report"
    _description = "Products In Transit Report"

    start_date = fields.Date(string='Starting Date', required='1', help='Select start date')
    end_date = fields.Date(string='Ending Date', required='1', help='Select eding date')
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
        
        products = self.env['stock.location'].search_read([("usage", "==", "Transit Location")]) 

        data = {
            'products': products,
        }

        return self.print_excel_report(data)

    def print_excel_report(self, data):
        return self.env.ref('nia_fiber_reports.action_products_in_transit_report_xlsx').report_action(self, data=data, config=False)
        