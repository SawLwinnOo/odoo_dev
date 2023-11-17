# -*- coding: utf-8 -*-
# from odoo import http


# class StationManagement(http.Controller):
#     @http.route('/station_management/station_management', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/station_management/station_management/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('station_management.listing', {
#             'root': '/station_management/station_management',
#             'objects': http.request.env['station_management.station_management'].search([]),
#         })

#     @http.route('/station_management/station_management/objects/<model("station_management.station_management"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('station_management.object', {
#             'object': obj
#         })

