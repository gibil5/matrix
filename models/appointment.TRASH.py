	#date_delay = fields.Float(
	#		compute='_compute_date_delay',
	#	)

	#@api.multi
	#@api.depends('patient')
	#def _compute_date_delay(self):
	#	for record in self:
	#		record.date_delay = 0.5






	#def move(self, appointment_date, delta_min):



# ----------------------------------------------- Dep --------------------------------
	#val = fields.Char()



	name = fields.Char(
			default='Cita',
		)


	date_start = fields.Datetime(
		'Hora',
		required=True,
	)


	patient = fields.Many2one(
		'matrix.patient',
		string='Paciente',
		required=True,
	)


	doctor = fields.Many2one(
		'matrix.doctor',
		string='Doctor',
		required=True,
	)


	app_type = fields.Selection(
			[
				('consultation', 	'Consulta'),
				('procedure', 		'Procedimiento'),
				('control', 		'Control'),
				('event', 			'Evento'),
			],
			string='Tipo',
			required=True,
		)

	state = fields.Selection(
			[
				('scheduled', 		'Confirmado'),
				('pre_scheduled', 	'No Confirmado'),
				('canceled', 		'Anulado'),
			],
			string='Estado',
			required=True,
		)


