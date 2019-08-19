# -*- coding: utf-8 -*-
from __future__ import print_function
from openerp import models, fields, api

class Project(models.Model):
	"""
	Project
	"""
	_name = 'matrix.project'

	name = fields.Char()

	task_ids = fields.One2many(
			'matrix.task',
			'project_id',
		)
