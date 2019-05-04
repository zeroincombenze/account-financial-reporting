# -*- coding: utf-8 -*-
# Copyright 2019 - Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>
#
# License LGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
# Code partially inherited by account_follow_up 8.0 of OCA
#
{
    'name': 'Customer Payment Follow-up Management',
    'version': '10.0.1.0.1',
    "license": "LGPL-3",
    'category': 'Accounting & Finance',
    'summary': 'Module to do followup on customer unpaid invoices.',
    'author': 'Odoo SA, SHS-AV s.r.l.',
    'website': 'www.probuse.com',
    'depends': [
        'account',
        'mail',
        'sales_team',
    ],
    'data': [
        'security/account_followup_security.xml',
        'security/ir.model.access.csv',
        'data/account_followup_data.xml',
        'views/account_followup_view.xml',
        'views/account_followup_customers.xml',
        'wizard/account_followup_print_view.xml',
        'views/res_config_view.xml',
        'report/report_followup.xml',
        'report/account_followup_reports.xml'
    ],
    'images': ['static/description/im2.jpg'],
    'demo': [],
    'installable': True,
    'auto_install': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
