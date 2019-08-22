# -*- coding: utf-8 -*-
from __future__ import print_function
from openerp import models, fields, api

class ColorField(models.Model):
	"""
	Slot
	"""
	_name = 'matrix.color_field'


	type = fields.Char(
			default='selection',
		)