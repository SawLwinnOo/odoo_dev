# -*- coding: utf-8 -*-
{
    'name': "station_management",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'author': "My Company",
    'website': "https://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'fleet'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',

        'data/sequence.xml',

        'views/booking.xml',
        'views/station.xml',
        'views/station_lane.xml',
        'views/menus.xml'

    ],
}
