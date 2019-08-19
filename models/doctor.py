# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Doctor(models.Model):

   _name = 'matrix.doctor'


   name = fields.Char()

   idx = fields.Integer()
