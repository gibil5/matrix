# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Appointment(models.Model):

	_name = 'matrix.appointment'

	
	name = fields.Char(
			default='Cita',
		)


	#date_start = fields.Float(
	date_start = fields.Datetime(
		'Hora',
		required=True,
	)


	patient = fields.Many2one(
		'matrix.patient',
		string='Paciente',
		required=True,
	)


	doctor = fields.Many2one(
		'matrix.doctor',
		string='Doctor',
		required=True,
	)


	app_type = fields.Selection(
			[
				('consultation', 	'Consulta'),
				('procedure', 		'Procedimiento'),
				('control', 		'Control'),
				('event', 			'Evento'),
			],
			string='Tipo',
			required=True,
		)

	state = fields.Selection(
			[
				('scheduled', 		'Confirmado'),
				('pre_scheduled', 	'No Confirmado'),
				('canceled', 		'Anulado'),
			],
			string='Estado',
			required=True,
		)


