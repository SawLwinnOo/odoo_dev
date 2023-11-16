# -*- coding: utf-8 -*-
# from odoo import http


# class GasStation(http.Controller):
#     @http.route('/gas_station/gas_station', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gas_station/gas_station/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('gas_station.listing', {
#             'root': '/gas_station/gas_station',
#             'objects': http.request.env['gas_station.gas_station'].search([]),
#         })

#     @http.route('/gas_station/gas_station/objects/<model("gas_station.gas_station"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gas_station.object', {
#             'object': obj
#         })

