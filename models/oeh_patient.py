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

