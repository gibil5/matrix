# -*- coding: utf-8 -*-
from __future__ import print_function
from openerp import models, fields, api

class User(models.Model):
	"""
	User
	"""
	_name = 'matrix.user'

	name = fields.Char()

	task_ids = fields.One2many(
			'matrix.task',
			'user_id',
		)
