{
    "name": "Liquor Store",
    "author": "Saw Lwinn Oo",
    "depends": ["sale", "mail", "website"],
    "data": [

        # security
        "security/ir.model.access.csv",
        "security/liquor_security.xml",

        # sequence
        "data/sequence.xml",
        "data/mail_template_sale_order.xml",

        # views
        "views/liquor_product.xml",
        "views/liquor_order.xml",
        "views/liquor_order_line.xml",
        "views/template.xml",

        # reports
        "report/liquor_order_report.xml",
        "report/report.xml",
        # menus
        "views/menus.xml"
    ],
    "license": "LGPL-3"
}
