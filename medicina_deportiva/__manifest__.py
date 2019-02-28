# -*- coding: utf-8 -*-
{
    'name': "Medicina_deportiva",

    'summary': """
        Controla las lesiones de tu equipo""",

    'description': """
        Este modulo nos ayuda a poder controlar el numero de lesiones y bajas en un equipo,
        de modo que podamos tener una mayor gestion sobre el estado de nuestros jugadores.
    """,

    'author': "Álvaro Díez",
    'website': "http://www.medicina_deportiva.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [

        'data/medicina_deportiva_data.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
