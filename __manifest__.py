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

{
    'name': "Nia Fiber Reports",
    'author': 'SIMI Technologies',
    'category': 'account_invoicing',
    'summary': """Accounting Reports for Nia Fiber""",
    'website': 'http://www.simitechnologies.co.ke',
    'license': 'AGPL-3',
    'description': """
""",
    'version': '15.0.1.0',
    'depends': ['base','account', 'report_xlsx'],
    'data': ['security/ir.model.access.csv',
             'wizard/product_invoice.xml',
             'wizard/purchase_invoice.xml',
             'wizard/inventory_aging_wizard.xml',
             'wizard/draft_po_wizard.xml',
             'wizard/draft_so_wizard.xml',
             'wizard/stock_quantity_wizard.xml',
             'wizard/stock_quantity_per_warehouse_wizard.xml',
             'wizard/stock_adjustment_wizard.xml',
             'wizard/chart_of_accounts_wizard.xml',
             'wizard/general_ledger_wizard.xml',
             'wizard/products_in_transit_wizard.xml',
             'wizard/balance_sheet_wizard.xml',
             'views/product_invoice_report_view.xml',
             'report/product_invoice_template.xml',
             'report/product_invoice_report.xml',
             'report/inventory_aging_report.xml',
             'report/draft_po_report.xml',
             'report/draft_so_report.xml',
             'report/purchase_invoice_report.xml',
             'report/stock_quantity_report.xml',
             'report/stock_quantity_per_warehouse_report.xml',
             'report/stock_adjustment_report.xml',
             'report/chart_of_accounts_report.xml',
             'report/general_ledger_report.xml',
             'report/products_in_transit_report.xml',
             'report/balance_sheet_report.xml',
             ],
    'installable': True,
    'images': ['static/description/banner.png'],
    'application': True,
    'auto_install': False,
}
