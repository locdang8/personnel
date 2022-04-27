# -*- coding: utf-8 -*-
# from odoo import http


# class Nhansu(http.Controller):
#     @http.route('/nhansu/nhansu/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/nhansu/nhansu/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('nhansu.listing', {
#             'root': '/nhansu/nhansu',
#             'objects': http.request.env['nhansu.nhansu'].search([]),
#         })

#     @http.route('/nhansu/nhansu/objects/<model("nhansu.nhansu"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('nhansu.object', {
#             'object': obj
#         })
