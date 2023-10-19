{
    'name': 'Product Portal',
    'author': 'Saw Lwinn Oo',
    'category': 'Sales',
    'summary': 'Portal Integration will empower users to see product counts easily, and maintain product templates easily, improving the overall sales process and customer experience',
    'depends': ['sale','website', 'portal'],
    'images': [
        'static/description/cover.png',
    ],
    'data': [
        #security
        # "security/ir.model.access.csv",
        # "security/sale_security.xml",
        #views
        "views/portal_template.xml",
    ],

    'license': 'LGPL-3',
}
