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

class Admin(Users):
	def __init__(self, first_name, last_name):
		super().__init__(first_name, last_name)
		self.privileges = Privileges()
	

class Privileges():
	def __init__(self,privileges=[]):
		self.privileges = privileges
	
	def show_privileges(self):
		print ('The administrator')
		for i in self.privileges:
			print ('-',i)
				
admin01 = Admin('Lisa','Li')
admin01.privileges.privileges = ['can add post','can delete post', 'can ban user']
admin01.privileges.show_privileges()				

