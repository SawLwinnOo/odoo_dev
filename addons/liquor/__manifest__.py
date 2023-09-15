{
    "name": "Liquor Store",
    "depends": ["sale", "mail"],
    "data":[

        #security
        "security/ir.model.access.csv",

        #sequence
        "data/sequence.xml",

        #views
        "views/liquor_product.xml",
        "views/liquor_order.xml",
        "views/liquor_order_line.xml",

        #reports
        "report/liquor_order_report.xml",
        "report/report.xml",
        #menus
        "views/menus.xml"
    ],
    "license": "LGPL-3"
}