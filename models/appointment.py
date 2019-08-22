# -*- coding: utf-8 -*-
import datetime
from openerp import models, fields, api
from . import app_funcs

class Appointment(models.Model):

	_name = 'matrix.appointment'




# ----------------------------------------------- Relational --------------------------------
	patient_id = fields.Many2one(
			'oeh.medical.patient',
			ondelete='cascade',
		)



# ----------------------------------------------- Remove  --------------------------------

	@api.multi
	def remove_myself(self):
		print()
		print('Remove Myself')

		rec_set = self.env['matrix.appointment'].browse([self.id])

		ret = rec_set.unlink()



# ----------------------------------------------- Update --------------------------------

	@api.multi
	def update(self):
		print()
		print('Update')

		if self.patient.name not in [False]:
			self.patient_pre = self.patient.name
			if self.patient.x_id_doc not in [False]:				
				self.dni_pre = self.patient.x_id_doc
			else:
				self.dni_pre = self.patient.x_dni




# ----------------------------------------------- Fields ---------------------------------------------

	patient = fields.Many2one(
			'oeh.medical.patient',
			#string='Paciente',
			string='Paciente Existe',
		)

	patient_pre = fields.Char(
			string='Paciente No existe',
		)

	dni_pre = fields.Char(
			'DNI',
		)




# ----------------------------------------------- Computes ----------------------------------------
	date_stop = fields.Datetime(
			compute='_compute_date_stop',
		)

	@api.multi
	#@api.depends('patient')
	def _compute_date_stop(self):
		for record in self:
			record.date_stop = app_funcs.time_delta(record, record.date_start, 30)


	date_delay = fields.Float(
			compute='_compute_date_delay',			
		)

	@api.multi
	#@api.depends('patient')
	def _compute_date_delay(self):
		for record in self:
			record.date_delay = 0.5


	x_display = fields.Char(
			compute='_compute_x_display',
		)

	@api.multi
	#@api.depends('patient')
	def _compute_x_display(self):
		for record in self:

			if record.patient.name not in [False]:
				record.x_display = record.patient.get_display_code() + ' ' + str(record.doctor.idx)

			else:
				record.x_display = record.patient_pre.replace(' ', '_') + ' ' + str(record.doctor.idx)


	
# ----------------------------------------------- Relational --------------------------------

	container_id = fields.Many2one(
			'matrix.container',
			ondelete='cascade',
		)


	doctor = fields.Many2one(
			'matrix.doctor',
			string='Doctor',
		)


# ----------------------------------------------- Fields ---------------------------------------------
	date_start = fields.Datetime(
			'Hora',
		)

	state = fields.Selection(
			[
				('pre_scheduled', 	'No Confirmado'),
				('scheduled', 		'Confirmado'),
			],
			string='Estado',
		)

	app_type = fields.Selection(
			[
				('consultation', 	'Consulta'),
				('procedure', 		'Procedimiento'),
				('control', 		'Control'),
				('event', 			'Evento'),
			],
			string='Tipo',
		)


	# Vspace
	vspace = fields.Char(
			' ',
			readonly=True
		)


