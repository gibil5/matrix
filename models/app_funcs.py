# -*- coding: utf-8 -*-

import datetime

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
