# -*- coding: utf-8 -*-
from odoo import http

# class LivresModule(http.Controller):
#     @http.route('/livres_module/livres_module/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/livres_module/livres_module/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('livres_module.listing', {
#             'root': '/livres_module/livres_module',
#             'objects': http.request.env['livres_module.livres_module'].search([]),
#         })

#     @http.route('/livres_module/livres_module/objects/<model("livres_module.livres_module"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('livres_module.object', {
#             'object': obj
#         })