class Users():
	"""docstring for Users"""
	def __init__(self,first_name,last_name):				
		self.first_name = first_name
		self.last_name = last_name
		self.age = 0 #initialized as 0
		self.gender = "female"
		#for exercise 9.5
		self.login_attempt = 0

	def increment_login_attemp(self):
		self.login_attempt += 1

	def reset_login_attemp(self):
		self.login_attempt = 0

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

n = int(input("How many times did he log in? "))
for i in range (0,n):
	user_1.increment_login_attemp()
	#print(user_1.login_attempt)
	i += 1
print("The user has tried to logged in",str(user_1.login_attempt),"times.")

user_1.reset_login_attemp()
print("Now the login attemp has been reset to",user_1.login_attempt,"")