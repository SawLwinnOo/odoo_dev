# -*- coding: utf-8 -*-
# from odoo import http


# class TravelDiary(http.Controller):
#     @http.route('/travel_diary/travel_diary', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/travel_diary/travel_diary/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('travel_diary.listing', {
#             'root': '/travel_diary/travel_diary',
#             'objects': http.request.env['travel_diary.travel_diary'].search([]),
#         })

#     @http.route('/travel_diary/travel_diary/objects/<model("travel_diary.travel_diary"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('travel_diary.object', {
#             'object': obj
#         })
