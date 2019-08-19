



	# Doctor Columns
	doctor_cha = fields.Many2one(
			'matrix.patient',
			string='Dr. Chavarri',
		)

	doctor_can = fields.Many2one(
			'matrix.patient',
			string='Dr. Canales',
		)
	
	doctor_abr = fields.Many2one(
			'matrix.patient',
			string='Dr. Abriojo',
		)

	doctor_gon = fields.Many2one(
			'matrix.patient',
			string='Dr. Gonzales',
		)

	doctor_mon = fields.Many2one(
			'matrix.patient',
			string='Dr. Monteverde',
		)

	doctor_esc = fields.Many2one(
			'matrix.patient',
			string='Dr. Escudero',
		)



	# Appointments
	app_cha = fields.Many2one(
			'matrix.appointment',
			'.',
		)

	app_can = fields.Many2one(
			'matrix.appointment',
			'.',
		)

	app_abr = fields.Many2one(
			'matrix.appointment',
			'.',
		)




	#patient = fields.Char()




# ----------------------------------------------- Functions --------------------------------
	@api.multi
	def create_app(self):
		print()
		print('Create App')

