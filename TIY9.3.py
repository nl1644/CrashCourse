class Users():
	"""docstring for Users"""
	def __init__(self,first_name,last_name):				
		self.first_name = first_name
		self.last_name = last_name
		self.age = 0 #initialized as 0
		self.gender = "female"

	def describe_user(self):
		print(self.first_name.title(),self.last_name.title(),"is",str(self.age),"years old.")
	def greet_user(self):
		fullName = self.first_name.title() + " " + self.last_name.title()
		print("Hi,",fullName+",","welcome to Python Crash Course.")

	# function to update the age attribute
	def update_age(self, age_now):
		self.age = age_now

		

user_1 = Users("mike","gavidia")
user_1.age = 39

# use the update_age function to update age
user_1.update_age(33)

# user_2 = Users("lisa","li")
# user_2.age = 20

# user_3 = Users("gloria","pezca")

user_1.describe_user()
user_1.greet_user()

# user_2.describe_user()
# user_2.greet_user()