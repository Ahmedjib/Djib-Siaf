# -*- coding: utf-8 -*-
{
    'name': 'SIAF Customisation',
    'version': '15.0.0.1.0',
    'category': 'Sales',
    'summary': 'SIAF Customisation',
    'description': """
        This module add extra stage to sale process for groups
        * Sales
        * MRP
        * Admin
        * MAINTENANCE
    """,
    'sequence': 1,
    'author': 'Ahmed Abdi',
    'website': 'https://ahmed.abdi.com/',
    'depends': ['base','sale_management', 'account','product'],
    'data': [
        'views/views.xml',
        'security/ir.model.access.csv',
    ],
    'images': [
        'static/description/logo.jpg',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': False,
    'license': 'LGPL-3'
}
