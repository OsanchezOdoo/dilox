# -*- coding: utf-8 -*-
{
    'name': "addenda_extra_odoo",

    'summary': """ """,

    'description': """
        
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '16.1.1',
    'depends': ['l10n_mx_edi','account'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/AddendaModelo.xml',
        'views/account_move_view.xml',
        'views/res_partner_view.xml',
        'views/account_payment_term_view.xml',
        'views/res_company_view.xml',
    ],
}
