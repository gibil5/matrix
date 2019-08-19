# -*- coding: utf-8 -*-
from __future__ import print_function
from openerp import models, fields, api

class Slot(models.Model):
	"""
	Slot
	"""
	_name = 'matrix.slot'




#----------------------------------------------------------- Hot Button - For Container ---------

	@api.multi
	def open_line_current(self):
		"""
		Hot Button. For Day Container.
		"""

		return {
				'type': 'ir.actions.act_window',

				'name': ' Edit Order Current',
				
				'view_type': 'form',
				
				'view_mode': 'form',
				
				'res_model': self._name,
				
				'res_id': self.id,
				
				'target': 'current',
				
				'flags': {
						#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
						'form': {'action_buttons': True, }
						},
				
				'context': {}
		}


# ----------------------------------------------- Relational --------------------------------

	container_id = fields.Many2one(
			'matrix.container',
			ondelete='cascade',
		)

	#container_cha_id = fields.Many2one(

	container_0_id = fields.Many2one(
			'matrix.container',
			ondelete='cascade',
		)

	container_1_id = fields.Many2one(
			'matrix.container',
			ondelete='cascade',
		)

	container_2_id = fields.Many2one(
			'matrix.container',
			ondelete='cascade',
		)


	container_3_id = fields.Many2one(
			'matrix.container',
			ondelete='cascade',
		)

	container_4_id = fields.Many2one(
			'matrix.container',
			ondelete='cascade',
		)

	container_5_id = fields.Many2one(
			'matrix.container',
			ondelete='cascade',
		)





# ----------------------------------------------- Relational --------------------------------
	#name = fields.Many2one(
	doctor = fields.Many2one(
			'matrix.doctor',
			string='Doctor',
			required=True,
		)

	# Patient
	patient = fields.Many2one(
			'matrix.patient',
			string='Paciente',
			required=True,
		)

	# Appointment
	#appointment = fields.Many2one(
	#		'matrix.appointment',
	#		'Cita',
	#	)


# ----------------------------------------------- Fields --------------------------------
	date = fields.Date(
			'Fecha',
			required=True,
			default=fields.Date.today,
		)

	#date_start = fields.Datetime()
	date_start = fields.Float(
			'Hora',
		)



	slot_type = fields.Selection(
			[
				('consultation', 	'Consulta'),
				('procedure', 		'Procedimiento'),
				('control', 		'Control'),
				('event', 			'Evento'),
			],
			string='Tipo',
			required=True,
			default='consultation',
		)

	state = fields.Selection(
			[
				('pre_scheduled', 	'No Confirmado'),
				('scheduled', 		'Confirmado'),
				#('canceled', 		'Anulado'),
			],
			string='Estado',
			required=True,
			default='pre_scheduled',
		)
