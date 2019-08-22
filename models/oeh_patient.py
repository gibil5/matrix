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
	high level support for doing this and that.
	"""
	_inherit = 'oeh.medical.patient'



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
