##############################################################################
#
#    Copyright (C) 2015  ADHOC SA  (http://www.adhoc.com.ar)
#    All Rights Reserved.
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
##############################################################################
{
    'name': 'Fast and Fresh Reports',
    'version': '11.0.1.4.0',
    'category': 'Localization/Argentina',
    'sequence': 14,
    'author': 'Calyx',
    'website': '',
    'license': 'AGPL-3',
    'summary': 'Reportes Personalizados para Fast & Fresh',
    'depends': [
        'l10n_ar_afipws_fe',
        'l10n_ar_aeroo_einvoice',
        'report_aeroo_extra_function',
        'account_invoice_sale_link',
    ],
    'external_dependencies': {
    },
    'data': [
        #'report_configuration_defaults_data.xml',
        'sale_order_report.xml',
        #'invoice_report.xml',
        #'invoice_template.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}

