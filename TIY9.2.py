class Restaurant():
	def __init__(self, name, cuisine_type):
		self.name = name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		print(self.name.title(), "serves", self.cuisine_type.title(), "food.")
	def open_restaurant(self):
		print(self.name.title(),"is now open.")

	# def set_number_served(self, n):
	# 	self.number_served = n
	
	# def increment_number_served(self, n):
	# 	if n > 0:
	# 		self.number_served += n
	# 	else:
	# 		print("Not a valid increment.")

restaurant = Restaurant("Cindy\'s","American")

print(restaurant.name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()
