# -*- coding: utf-8 -*-
from openerp import http

# class Matrix(http.Controller):
#     @http.route('/matrix/matrix/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/matrix/matrix/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('matrix.listing', {
#             'root': '/matrix/matrix',
#             'objects': http.request.env['matrix.matrix'].search([]),
#         })

#     @http.route('/matrix/matrix/objects/<model("matrix.matrix"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('matrix.object', {
#             'object': obj
#         })