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

        #menus
        "views/menus.xml"
    ]
}