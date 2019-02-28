# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import *

class jugador(models.Model):
    _name = 'medicina_deportiva.jugador'

    nombre = fields.Char(string = "Nombre", required = True)
    name = fields.Char(string  = "DNI", required = True)
    apellidos = fields.Char(string="Apellidos", required = True)
    edad = fields.Integer(string="Edad", required = True)
    lesiones = fields.Integer(compute = "_value_lesiones", string = "Numero lesiones")
    lesion = fields.One2many("medicina_deportiva.lesion","jugador",string = "Lesiones")

    @api.one
    @api.depends('lesion')
    def _value_lesiones(self):
        self.lesiones = len(self.lesion)

class medico(models.Model):
    _name = 'medicina_deportiva.medico'

    nombre = fields.Char(string = "Nombre", required = True)
    name = fields.Char(string  = "DNI", required = True)
    apellidos = fields.Char(string="Apellidos", required = True)
    edad = fields.Integer(string="Edad", required = True)



class lesion(models.Model):
    _name = 'medicina_deportiva.lesion'

    nombre = fields.Char(string = "Nombre de lesion", required = True)
    name = fields.Char(string  = "IDENTIFICADOR", required = True)
    fecha = fields.Date(string = "Fecha de la lesion", required = True)
    tiempo_recuperacion = fields.Integer(string = "Dias de recuperacion de la lesion", required = True)
    jugador = fields.Many2one("medicina_deportiva.jugador",string="Jugador")
    medico = fields.Many2many("medicina_deportiva.medico", string="medico")
