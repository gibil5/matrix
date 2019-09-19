# -*- coding: utf-8 -*-
import datetime
from openerp import models, fields, api

from . import app_funcs

class Appointment(models.Model):

	_name = 'matrix.appointment'

	_order = 'date_start desc'

	_description = 'Matrix Appointment'




# ----------------------------------------------- On changes ---------------------------------------------
	# On Change Dni
	@api.onchange('dni_pre')
	def _onchange_dni_pre(self):

		#self.patient = ord_funcs.search_patient_by_id_document(self)
		self.patient = app_funcs.search_patient_by_id_document(self)




# ----------------------------------------------- Fields ---------------------------------------------

	comment = fields.Text(

			'Comentario',
		)






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




# ----------------------------------------------- Natives ---------------------------------------------


	name = fields.Char(
			'Nombre',
			compute='_compute_name',
		)

	@api.multi
	def _compute_name(self):

		sep = '-'

		for record in self:

			record.name = record.patient.get_display_code() + sep + record.doctor.name + sep + record.app_type





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
			index=False,

			compute='_compute_date_stop',
		)

	@api.multi
	#@api.depends('patient')
	def _compute_date_stop(self):
		for record in self:
			record.date_stop = app_funcs.time_delta(record, record.date_start, record.delta_min)


	delta_min = fields.Selection(
			[
				(30, '30 min'),
				(15, '15 min'),
				(60, '60 min'),
			],
			string='Duracion',
		)


	x_display = fields.Char(
			compute='_compute_x_display',
		)

	@api.multi
	#@api.depends('patient')
	def _compute_x_display(self):
		_dic_state = {
						'scheduled': 'C',
						'pre_scheduled': 'N',
		}
		for record in self:
			if record.patient.name not in [False]:
				#record.x_display = record.patient.get_display_code() + ' ' + str(record.doctor.idx) +  ' ' +  _dic_state[record.state]
				record.x_display = record.patient.get_display_code() + '-' + record.get_dni_display_code() + ' ' + str(record.doctor.idx) +  ' ' +  _dic_state[record.state]

			else:
				record.x_display = record.patient_pre.replace(' ', '_') + ' ' + str(record.doctor.idx) +  ' ' +  _dic_state[record.state]




# ----------------------------------------------- Get Display Code --------------------------------

	#@api.multi
	def get_dni_display_code(self):
		#print()
		#print('Get Display Code')

		if self.dni_pre not in [False]:
			code = self.dni_pre 
		else:
			code = 'x'

		return code



	
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
			#'Hora',
			'Fecha',
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
				('event', 			'Reunion'),
			],
			string='Tipo',
		)

	# Vspace
	vspace = fields.Char(
			' ',
			readonly=True
		)



# ----------------------------------------------- Test - Class Methods --------------------------------
	@classmethod

	#def cmethod():
	def cmethod(self):

		s = 'Class Method'

		return s


	@staticmethod
	
	def smethod():

		s = 'Static Method'

		return s
