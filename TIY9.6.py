class Restaurant():
	def __init__(self, name, cuisine_type):
		self.name = name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		print(self.name.title(), "serves", self.cuisine_type.title(), "food.")
	
	def open_restaurant(self):
		print("The restaurant is now open.")

	def set_number_served(self, n):
		self.number_served = n
	
	def increment_number_served(self, n):
		if n > 0:
			self.number_served += n
		else:
			print("Not a valid increment.")

class IceCreamStand(Restaurant):
	"""docstring for IceCreamStand"""
	def __init__(self, name, cuisine_type):
		super().__init__(name, cuisine_type)
		self.flavors = [] # has to be within this super().__init__(arg)

	def describe_flavor(self):
		print('\nThe flavors we serve are:\n')
		for i in self.flavors:
			print('- ',i.title())


icecreamstand = IceCreamStand("cauldren","froyo")
icecreamstand.flavors = ['lemon','cake batter','vanilla','chocalate','banana']
icecreamstand.describe_flavor()



