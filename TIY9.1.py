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

rstrt01 = Restaurant("cindy's", "american")

print(str(rstrt01.number_served),"people have been served.")

rstrt01.set_number_served(20)
print(str(rstrt01.number_served),"people have been served since update.")

rstrt01.increment_number_served(-3)
print(str(rstrt01.number_served),"people have been served for the day.")


