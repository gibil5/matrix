# 27 Sep 2019




# ----------------------------------------------- Relational --------------------------------
	appointment_ids = fields.One2many(
								'matrix.appointment', 
								'patient_id',
								#default=_default_app_ids,
							)


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

			app.patient_id = self.id


