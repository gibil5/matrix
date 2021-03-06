# -*- coding: utf-8 -*-
import datetime
from openerp import models, fields, api
from . import app_funcs

class Appointment(models.Model):
	_name = 'matrix.appointment'
	_order = 'date_start desc'
	_description = 'Matrix Appointment'



# ----------------------------------------------- Computes ---------------------------------------------

	# Name
	name = fields.Char(
			'Nombre',

			#compute='_compute_name',
		)

	@api.multi
	def _compute_name(self):
		se = '-'
		for record in self:
			if record.patient.name not in [False]:
				record.name = record.patient.get_display_code() + se + record.doctor.get_display_code() + se + record.get_type_code() + se + record.get_date_code()
			else:
				#record.name = record.get_comment_code() + se + record.doctor.get_display_code() + se + record.get_type_code() + se + record.get_date_code()
				record.name = record.get_patient_pre_code() + se + record.doctor.get_display_code() + se + record.get_type_code() + se + record.get_date_code()





	# Display
	x_display = fields.Char(

			compute='_compute_x_display',
		)

	@api.multi
	def _compute_x_display(self):
		_dic_state = {
						'scheduled': 'C',
						'pre_scheduled': 'N',
		}
		for record in self:

			# Patient exists in DB
			if record.patient.name not in [False]:
				#record.x_display = record.patient.get_display_code() + ' ' + str(record.doctor.idx) +  ' ' +  _dic_state[record.state]
				record.x_display = record.patient.get_display_code() + ' ' + str(record.doctor.idx) +  ' ' +  record.get_type_code()


			# Does not exist
			else:
				#record.x_display = record.get_patient_pre_code() + ' ' + str(record.doctor.idx) +  ' ' +  _dic_state[record.state]
				record.x_display = record.get_patient_pre_code() + ' ' + str(record.doctor.idx) +  ' ' +  record.get_type_code()




	# Date stop
	date_stop = fields.Datetime(
			index=False,

			compute='_compute_date_stop',
		)

	@api.multi
	#@api.depends('patient')
	def _compute_date_stop(self):
		for record in self:
			record.date_stop = app_funcs.time_delta(record, record.date_start, record.delta_min)





# ----------------------------------------------- Getters --------------------------------

	# Get Type
	def get_type_code(self):
		_dic = {
					#'consultation': 	'Consulta',
					#'procedure': 		'Procedimiento',
					#'control': 			'Control',
					#'event': 			'Reunion',
					'consultation': 	'Con',
					'procedure': 		'Pro',
					'control': 			'Ctl',
					'event': 			'Reu',
		}
		code = _dic[self.app_type]
		return code




	# Get Patient Pre Code
	def get_patient_pre_code(self):
		if self.patient_pre not in [False]:
			words = self.patient_pre.split()
			if len(words) > 1:
				code = words[0] + '_' + words[1]
			else:
				code = words[0]
		else:
			code = 'x'
		return code


	# Get DNI Code
	def get_dni_display_code(self):
		if self.dni_pre not in [False]:
			code = self.dni_pre 
		else:
			code = 'x'
		return code


	# Get Comment Code
	def get_comment_code(self):
		if self.comment not in [False]:
			words = self.comment.split()
			code = words[0]
		else:
			code = 'x'
		return code





	# Get Date
	def get_date_code(self):
		code = self.date_start
		code = app_funcs.time_delta(self, self.date_start, -300)
		return code



# ----------------------------------------------- Oeh Patient ---------------------------------------------
	patient_mat = fields.Many2one(
			'oeh.medical.patient',
			#string='Paciente',
		)

# ----------------------------------------------- Natives ---------------------------------------------

	patient = fields.Many2one(
			'oeh.medical.patient',
			string='Paciente Existe',
		)

	patient_pre = fields.Char(
			string='Paciente NO existe',
		)

	patient_exists = fields.Boolean(
			'Paciente Existe ?',
			default=True,
		)

	dni_pre = fields.Char(
			'DNI',
		)






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









# ----------------------------------------------- Computes ----------------------------------------

	delta_min = fields.Selection(
			[
				(30, '30 min'),
				(15, '15 min'),
				#(60, '60 min'),
			],
			string='Duracion',
		)









	
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

