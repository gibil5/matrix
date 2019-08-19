# -*- coding: utf-8 -*-
from __future__ import print_function
from openerp import models, fields, api

class Container(models.Model):
	"""
	Container
	"""
	_name = 'matrix.container'



# ----------------------------------------------- Relational --------------------------------

	slot_0_ids = fields.One2many(
									'matrix.slot', 
									'container_0_id',
							)

	slot_1_ids = fields.One2many(
									'matrix.slot', 
									'container_1_id',
							)

	slot_2_ids = fields.One2many(
									'matrix.slot', 
									'container_2_id',
							)


	slot_3_ids = fields.One2many(
									'matrix.slot', 
									'container_3_id',
							)

	slot_4_ids = fields.One2many(
									'matrix.slot', 
									'container_4_id',
							)

	slot_5_ids = fields.One2many(
									'matrix.slot', 
									'container_5_id',
							)



# ----------------------------------------------- Update --------------------------------

	@api.multi
	def update(self):
		print()
		print('Update')

		# Init

		#idx_arr = [0, 1, 2]
		idx_arr = [0, 1, 2, 3, 4, 5]

		_slot_handle = {
							0: self.slot_0_ids,
							1: self.slot_1_ids,
							2: self.slot_2_ids,

							3: self.slot_3_ids,
							4: self.slot_4_ids,
							5: self.slot_5_ids,
		}
		_container_id = {
							0: 'container_0_id',
							1: 'container_1_id',
							2: 'container_2_id',

							3: 'container_3_id',
							4: 'container_4_id',
							5: 'container_5_id',
		}

		# Clean
		#self.slot_0_ids.unlink()
		for idx in idx_arr:
			_slot_handle[idx].unlink()




		for slot in self.slot_ids:
			
			#if slot.doctor.name in ['Dr. Chavarri']:



			for idx in idx_arr:
	
				if slot.doctor.idx in [idx]:
					print(slot.doctor.name)

					#obj = self.slot_0_ids.create({
					obj = _slot_handle[idx].create({
														'doctor': slot.doctor.id,
														'date_start': slot.date_start,

														#'container_0_id': self.id,
														_container_id[idx]: self.id,
							})



# ----------------------------------------------- Fields --------------------------------

	#name = fields.Char()

	doctor = fields.Many2one(
			'matrix.doctor',
			string='Doctor',
		)

		
	date = fields.Date(
			'Fecha',
			#required=True,
			default=fields.Date.today, 
		)


	# Slots
	def _default_slot_ids(self):
		print()
		print('Default Slot Ids')

		# Slots
		slots = [	9, 9.5, 10, 10.5, 11, 11.5, 
					12, 12.5, 13, 13.5, 14, 14.5, 15, 15.5, 
					16, 16.5, 17, 17.5, 18, 18.5,
					17, 17.5, 18, 18.5, 19, 19.5, 
					20, 20.5, 21, 21.5, 
					#22,
				]

		# Doctors
		#doctors = self.env['matrix.doctor'].browse([1, 2, 3])
		doctors = self.env['matrix.doctor'].browse([1, 2, 3, 4, 5, 6])
		print(doctors)

		return [
				(0, 0, {
							#'date': self.date,
							'date_start': s,
							#'name': d.id, 
							'doctor': d.id, 
				})
				for d in doctors
				for s in slots
		]


	slot_ids = fields.One2many(
								'matrix.slot', 
								'container_id',
								#string='slot_ids',
								default=_default_slot_ids,
							)







