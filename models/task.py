# -*- coding: utf-8 -*-
from __future__ import print_function
from openerp import models, fields, api

class Task(models.Model):
	"""
	Task
	"""
	_name = 'matrix.task'


	name = fields.Char(
		)

	planned_hours = fields.Integer(
		)

	project_id = fields.Many2one(
			'matrix.project',
		)

	user_id = fields.Many2one(
			'matrix.user',
		)
