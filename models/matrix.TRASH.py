


	@api.multi
	def open_x2m_matrix(self):
		print()
		print('Open 2m matrix')

		#wiz = self.env['x2m.matrix.demo.wiz'].create({})
		wiz = self.env['matrix.wizard'].create({})

		print(wiz)

		#return {
		#		'name': 'Try x2many 2D matrix widget',
		#		'type': 'ir.actions.act_window',
		#		'view_type': 'form',
		#		'view_mode': 'form',
				#'res_model': 'x2m.matrix.demo.wiz',
		#		'res_model': 'matrix.wizard',		
		#		'target': 'new',
		#		'res_id': wiz.id,
		#		'context': self.env.context,
		#}




