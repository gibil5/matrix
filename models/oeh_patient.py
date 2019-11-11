# -*- coding: utf-8 -*-
"""
		Patient

 		Created: 		21 Aug 2019
		Last up: 		21 Aug 2019
"""
from __future__ import print_function
from openerp import models, fields, api

class Patient(models.Model):
	"""
	Patient Class. Inherited from OeHealth.
	"""
	_inherit = 'oeh.medical.patient'

	#from . import appointment


# ----------------------------------------------- App --------------------------------

	mat_appointment_ids = fields.One2many(
		
			'matrix.appointment',

			'patient_mat',

			#string="Citas",
		)



# ----------------------------------------------- Update --------------------------------
	
	@api.multi
	def update(self):
		print()
		print('Update')


		# Mat
		self.update_appointments_mat('matrix.appointment')

		self.update_controls('openhealth.control')


		# Native
		self.update_sales('sale.order')

		self.update_consultations('openhealth.consultation')

		self.update_procedures('openhealth.procedure')

		self.update_nr_ofs()




# ----------------------------------------------- Update App --------------------------------
	@api.multi
	def update_appointments_mat(self, model):
		"""
		Update Procedures
		"""
		print()
		print('Update Procedures')


		# Clean
		self.mat_appointment_ids.unlink()


		# Search
		objs = self.env[model].search([
										('patient', 'in', [self.name]),
										#('state', 'in', ['sale']),
									],
										#order='x_date_record desc',
										#limit=self.configurator.patient_limit,
									)
		print(objs)


		for obj in objs:
			#print(obj.patient.name)


			# Create
			appointment = self.mat_appointment_ids.create({
															'date_start': 	obj.date_start,

															'patient': 		obj.patient.id,												
															'doctor': 		obj.doctor.id,

															'state': 		obj.state,
															'app_type': 	obj.app_type,
															'delta_min': 	obj.delta_min,

															'patient_mat': self.id,
							})









# ----------------------------------------------- Get Display Code --------------------------------

	#@api.multi
	def get_display_code(self):
		print()
		print('Get Display Code')

		if self.name not in [False]:

			words = self.name.split()
			
			if len(words) > 1:
				code = words[0] + '_' + words[1]

			else:
				code = words[0]

		else:
			code = 'x'

		return code



