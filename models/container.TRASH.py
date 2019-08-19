

# ----------------------------------------------- Fields --------------------------------

	slot_0 = fields.Char(
			string='09:00',
		)

	slot_1 = fields.Char(
			string='09:30',
		)

	slot_2 = fields.Char(
			string='10:00',
		)



	slot_0_doctor_0 = fields.Many2one(
			'matrix.patient',
			string='09:00',
		)

	slot_1_doctor_0 = fields.Many2one(
			'matrix.patient',
			string='09:30',
		)

	slot_2_doctor_0 = fields.Many2one(
			'matrix.patient',
			string='10:00',
		)


	slot_0_doctor_1 = fields.Many2one(
			'matrix.patient',
			string='.',
		)
	slot_1_doctor_1 = fields.Many2one(
			'matrix.patient',
			string='.',
		)
	slot_2_doctor_1 = fields.Many2one(
			'matrix.patient',
			string='.',
		)


	slot_0_doctor_2 = fields.Many2one(
			'matrix.patient',
			string='.',
		)
	slot_1_doctor_2 = fields.Many2one(
			'matrix.patient',
			string='.',
		)
	slot_2_doctor_2 = fields.Many2one(
			'matrix.patient',
			string='.',
		)



	slot_0_doctor_3 = fields.Many2one(
			'matrix.patient',
			string='.',
		)
	slot_1_doctor_3 = fields.Many2one(
			'matrix.patient',
			string='.',
		)
	slot_2_doctor_3 = fields.Many2one(
			'matrix.patient',
			string='.',
		)
