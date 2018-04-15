class Car():
	"""docstring for Car"""
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
	
	def get_descriptive_name(self):
		'''return a neatly formatted descriptive name'''
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()

	def read_odometer(self):
		print('This car has' + str(self.odometer_reading) + 'miles on it.')

	def update_odo(self, mileage):
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print('Don\'t roll back an odometer!')

	def increment_odo(self,miles):
		self.odometer_reading += miles
		

		