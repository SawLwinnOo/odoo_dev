{
    "name":"My Note",
    "author": "Saw Lwinn Oo",
    "depends":["web"],
    "data": [
        #security
        "security/ir.model.access.csv",

        #views
        "views/my_note.xml",
    ],
    "license": "LGPL-3",
    'assets': {
        'web.assets_backend': [
            "my_note/static/src/note/my_note.js",
            "my_note/static/src/note/my_note.xml",
        ],
    },
}