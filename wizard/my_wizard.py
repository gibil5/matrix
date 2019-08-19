# -*- coding: utf-8 -*-
from openerp import models, fields, api

class MyWizard(models.TransientModel):
   #_name = 'my.wizard'
   _name = 'matrix.wizard'


   def _default_task_ids(self):
	   # your list of project should come from the context, some selection
	   # in a previous wizard or wherever else

	   print()
	   print('Default Task Ids')

	   #projects = self.env['project.project'].browse([1, 2, 3])
	   projects = self.env['matrix.project'].browse([1, 2, 3])
	   print(projects)

	   # same with users
	   #users = self.env['res.users'].browse([1, 2, 3])
	   users = self.env['matrix.user'].browse([1, 2, 3])
	   print(users)

	   return [
			   (0, 0, {
		                'name': 'Sample task name',
			   			'project_id': p.id, 
			   			'user_id': u.id, 
			   			'planned_hours': 0
			   		})
			   # if the project doesn't have a task for the user, create a new one
			   if not p.task_ids.filtered(lambda x: x.user_id == u) else
			   # otherwise, return the task
			   (4, p.task_ids.filtered(lambda x: x.user_id == u)[0].id)
			   for p in projects
			   for u in users
	   ]

   #task_ids = fields.Many2many('matrix.task')
   task_ids = fields.Many2many('matrix.task', default=_default_task_ids)

