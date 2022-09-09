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

class DraftPOReport(models.TransientModel):
    _name = "draft.po.report"
    _description = "Draft PO Report"

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
        startDate = self.read(['start_date'])
        endDate = self.read(['end_date'])
        products = self.env['purchase.order.line'].search_read([('state', '=', 'draft')]) 

        data = {
            'products': products,
            'form_data': self.read(['start_date', 'end_date']),
            'start_date': startDate,
            'end_date': endDate
        }

        return self.print_excel_report(data)

    def print_excel_report(self, data):
        return self.env.ref('nia_fiber_reports.action_draft_po_report_xlsx').report_action(self, data=data, config=False)
        