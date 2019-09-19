# -*- coding: utf-8 -*-

import datetime



# ----------------------------------------------------------- Getters -------------------------
def search_patient_by_id_document(self):
	print()
	print('Search Patient')

	# Protect against On change first time calls
	if self.dni_pre != False:

		# Search Patient - by ID IDOC
		patient = self.env['oeh.medical.patient'].search([
															('x_id_doc', '=', self.dni_pre),
											],
												order='write_date desc',
												limit=1,
											)

		# Search Patient - by DNI
		if patient.name == False:

			patient = self.env['oeh.medical.patient'].search([
																('x_dni', '=', self.dni_pre),
												],
													order='write_date desc',
													limit=1,
												)
		#print(patient.name)


		return patient.id

	else:
		return False





# ----------------------------------------------- Time Funcs --------------------------------
#@api.multi
def time_delta(self, appointment_date, delta_min):
	"""
	Time Delta
	"""
	date_format = "%Y-%m-%d %H:%M:%S"
	new_dt = datetime.datetime.strptime(appointment_date, date_format) + datetime.timedelta(hours=0, minutes=delta_min)
	new_str = new_dt.strftime(date_format)
	return new_str
