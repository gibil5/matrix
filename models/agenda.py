# -*- coding: utf-8 -*-
from __future__ import print_function
from openerp import models, fields, api

class Agenda(models.Model):
	"""
	Agenda
	"""
	_name = 'matrix.agenda'



# ----------------------------------------------- Relational --------------------------------
	doctor = fields.Many2one(
			'matrix.doctor',
			string='Hora',
		)


	# Slots
	slot_0 = fields.Many2one(
			'matrix.patient',
			string='09:00',
		)

	slot_1 = fields.Many2one(
			'matrix.patient',
			string='09:30',
		)

	slot_2 = fields.Many2one(
			'matrix.patient',
			string='10:00',
		)

	slot_3 = fields.Many2one(
			'matrix.patient',
			string='10:30',
		)



	slot_4 = fields.Many2one(
			'matrix.patient',
			string='11:00',
		)

	slot_5 = fields.Many2one(
			'matrix.patient',
			string='11:30',
		)

	slot_6 = fields.Many2one(
			'matrix.patient',
			string='12:00',
		)

	slot_7 = fields.Many2one(
			'matrix.patient',
			string='12:30',
		)

	slot_8 = fields.Many2one(
			'matrix.patient',
			string='13:00',
		)






	slot_9 = fields.Many2one(
			'matrix.patient',
			string='13:30',
		)

	slot_10 = fields.Many2one(
			'matrix.patient',
			string='14:00',
		)

	slot_11 = fields.Many2one(
			'matrix.patient',
			string='14:30',
		)

	slot_12 = fields.Many2one(
			'matrix.patient',
			string='15:00',
		)

	slot_13 = fields.Many2one(
			'matrix.patient',
			string='15:30',
		)




	slot_14 = fields.Many2one(
			'matrix.patient',
			string='16:00',
		)

	slot_15 = fields.Many2one(
			'matrix.patient',
			string='16:30',
		)

	slot_16 = fields.Many2one(
			'matrix.patient',
			string='17:00',
		)

	slot_17 = fields.Many2one(
			'matrix.patient',
			string='17:30',
		)

	slot_18 = fields.Many2one(
			'matrix.patient',
			string='18:00',
		)

	slot_19 = fields.Many2one(
			'matrix.patient',
			string='18:30',
		)




	slot_20 = fields.Many2one(
			'matrix.patient',
			string='19:00',
		)

	slot_21 = fields.Many2one(
			'matrix.patient',
			string='19:30',
		)

	slot_22 = fields.Many2one(
			'matrix.patient',
			string='20:00',
		)

	slot_23 = fields.Many2one(
			'matrix.patient',
			string='20:30',
		)

	slot_24 = fields.Many2one(
			'matrix.patient',
			string='21:00',
		)

	slot_25 = fields.Many2one(
			'matrix.patient',
			string='21:30',
		)

	slot_26 = fields.Many2one(
			'matrix.patient',
			string='22:00',
		)



# ----------------------------------------------- Fields --------------------------------
	name = fields.Char()

	date = fields.Date(
			'Fecha',
			required=True,
			default=fields.Date.today,
		)

	#date_start = fields.Datetime()
	#date_start = fields.Float(
	#		'Hora',
	#	)

