# -*- coding: utf-8 -*-
from odoo import http

# class MedicinaDeportiva(http.Controller):
#     @http.route('/medicina_deportiva/medicina_deportiva/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/medicina_deportiva/medicina_deportiva/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('medicina_deportiva.listing', {
#             'root': '/medicina_deportiva/medicina_deportiva',
#             'objects': http.request.env['medicina_deportiva.medicina_deportiva'].search([]),
#         })

#     @http.route('/medicina_deportiva/medicina_deportiva/objects/<model("medicina_deportiva.medicina_deportiva"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('medicina_deportiva.object', {
#             'object': obj
#         })