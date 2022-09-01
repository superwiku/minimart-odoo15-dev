# -*- coding: utf-8 -*-
# from odoo import http


# class Delfimart(http.Controller):
#     @http.route('/delfimart/delfimart/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/delfimart/delfimart/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('delfimart.listing', {
#             'root': '/delfimart/delfimart',
#             'objects': http.request.env['delfimart.delfimart'].search([]),
#         })

#     @http.route('/delfimart/delfimart/objects/<model("delfimart.delfimart"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('delfimart.object', {
#             'object': obj
#         })
