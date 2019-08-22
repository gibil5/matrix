# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Doctor(models.Model):

	_name = 'matrix.doctor'

	_order = 'idx asc'



	name = fields.Char()

	idx = fields.Integer()

	active = fields.Boolean(
		default=True,
	)


