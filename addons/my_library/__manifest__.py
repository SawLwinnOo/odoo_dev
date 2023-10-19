# -*- coding: utf-8 -*-
{
    'name': "My Library",

    'author': "Saw Lwinn Oo",
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'website'],

    # always loaded
    'data': [
        'security/group.xml',
        'security/ir.model.access.csv',
        'views/library_book.xml',
        'views/templates.xml',
        # 'views/snippets.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            # 'my_library/static/src/js/snippets.js',
        ],},
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
