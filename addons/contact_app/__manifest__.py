{
    "name": "Contacts",
    "author": "Saw Lwin Oo",
    "depends": ["base", "web"],
    'data': [
        "views/home.xml"
    ],
    'assets': {
        'contact_app.assets_standalone_app': [
            ('include', 'web._assets_helpers'),
            'web/static/src/scss/pre_variables.scss',
            'web/static/lib/bootstrap/scss/_variables.scss',
            ('include', 'web._assets_bootstrap'),

            ('include', 'web._assets_core'),
            'contact_app/static/src/**/*',
            'contact_app/static/src/app.js',
        ],
    }

}
