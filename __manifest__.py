# -*- coding: utf-8 -*-
{
    'name': "alumnos",

    'summary': "Gestion de matriculación de alumnos en módulos",

    'description': """
Gestión de matriculación de alumnos en módulos. Se pueden introducir los alumnos
y tambien los módulos en los que están matriculados. Relación Many2Many
    """,

    'author': "JMC",
    'website': "https://www.google.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Productivity',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/alumnos_views.xml',
        'views/modulos_views.xml',
        'views/menus.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
}

