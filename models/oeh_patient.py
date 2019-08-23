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



# ----------------------------------------------- Update Apps --------------------------------

	@api.multi
	def update_appointments(self):
		print()
		print('Update Apps')


		# Doctors
		apps = self.env['matrix.appointment'].search([
															('patient', 'in', [self.name]),
											],
												#order='x_serial_nr asc',
												#limit=1,
											)
		#print(apps)

		for app in apps:

			#print(app.patient.name)

			app.patient_id = self.id


			#obj = self.appointment_ids.create({
			#									'patient': app.patient.id,
			#									'doctor': app.doctor.id,
			#									'date_start': slot.date_start,
			#									patient_id: self.id,
			#				})






# ----------------------------------------------- Relational --------------------------------
	appointment_ids = fields.One2many(
								'matrix.appointment', 
								'patient_id',
								#default=_default_app_ids,
							)



# ----------------------------------------------- Get Display Code --------------------------------

	#@api.multi
	def get_display_code(self):
		#print()
		#print('Get Display Code')

		words = self.name.split()
		
		code = words[0] + '_' + words[1]

		return code
