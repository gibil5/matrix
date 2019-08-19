# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Patient(models.Model):

   _name = 'matrix.patient'

   name = fields.Char()
