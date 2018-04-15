class Car():
	def __init__(self, name, model, year):
		self.name = name
		self.model = model
		self.year = year

class Battery ():
	def __init__(self, battery_size = 90):
		self.battery_size = battery_size
	def upgrade_battery(self):
		if self.battery_size != 85:
			self.battery_size = 85
			print('Battery upgraded to', self.battery_size)
		else:
			return 
			self.battery_size

	
class ECar(Car):
	def __init__(self, name, model, year):
		super().__init__(name, model, year)
		self.battery = Battery()
	def desc_car(self):
		print(self.name.title(),self.model.title(),self.year)
	def get_range(self):
		if self.battery.battery_size == 70:
			print('The range is 300.')
		elif self.battery.battery_size == 85:
			print('The range is 450.')
		else:
			print('We don\'nt have data for your battery type.')


MyEcar = ECar('tesla','model 3','2018')

MyEcar.desc_car()
MyEcar.get_range()
MyEcar.battery.upgrade_battery()

MyEcar.get_range()		

		

