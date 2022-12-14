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

class InventoryAgingReport(models.TransientModel):
    _name = "inventory.aging.report"
    _description = "Inventory Aging Report"

    start_date = fields.Date(string='Starting Date', required='1', help='Select start date')
    period = fields.Integer(string='Period Length (Days)', required='1', help='Enter a period length.', default=30)
    limit = fields.Integer(string='Limit (Days)', required='1', help='Enter a limit.This is the maximum number of days that should be computed.', default=150)

    selection = fields.Selection([('payable', 'Payable Accounts'), ('receivable', 'Receivable Accounts'), ('all', 'All Accounts')], string="Account", required='1')

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
        startDate = self.read(['start_date'])[0]
        selection = self.read(['selection'])[0]
        
        if(selection['selection'] == 'payable'):
            products = self.env['account.move'].search_read([('invoice_date_due', '<=', startDate['start_date']), ('journal_id', '=', 'Vendor Bills'), ('state', '=', 'posted')]) 

        elif(selection['selection'] == 'receivable'):
            products = self.env['account.move'].search_read([('invoice_date_due', '<=', startDate['start_date']), ('journal_id', '=', 'Customer Invoices'), ('state', '=', 'posted')]) 

        else:
            products = self.env['account.move'].search_read([('invoice_date_due', '<=', startDate['start_date']), ('state', '=', 'posted')]) 

        data = {
            'products': products,
            'selection': selection,
            'form_data': self.read(['start_date', 'period', 'limit'])[0]
        }

        return self.print_excel_report(data)

    def print_excel_report(self, data):
        return self.env.ref('nia_fiber_reports.action_inventory_aging_report_xlsx').report_action(self, data=data, config=False)
        