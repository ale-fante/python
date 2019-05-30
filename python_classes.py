class Dog():
	"""A simple attempt to model a dog. """

	def __init__(self, name, age):
		"""Initialize name and age attributes."""
		self.name = name
		self.age = age

	def sit(self):
		"""Simulate a dog sitting in response to command."""
		print(self.name.title() + " is now sitting.")

	def roll(self):
		"""Simulate rolling over in response to a command."""
		print(self.name.title() + " rolled over!")

my_dog = Dog("Chiru", 6)

print("My Dog's name is " + my_dog.name + ".")
print(my_dog.name + " is " + str(my_dog.age) + " years old.")
my_dog.sit()
my_dog.roll()

# --------------------------------------------------------------

class Restaurant():
	"""Restaurant class"""

	def __init__(self, resturant_name, cuisine_type):
		"""Initialize the name and type attributes"""
		self.resturant_name = resturant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		"""Print restaurant name and food type"""
		print("The name of the restaurant is " + self.resturant_name.title())
		print("They serve " + self.cuisine_type.title() + " food.")

	def open_restaurant(self):
		"""Indicate whether the restaurant is open"""
		print(self.resturant_name.title() + " is open for business!")

restaurant = Restaurant("Don Cucos", "Mexican")

print("My favorite restaurant is " + restaurant.resturant_name)
print(restaurant.resturant_name + " serves " + restaurant.cuisine_type + " food.")

#Restaurant.describe_restaurant()
Restaurant("Pho Hut", "Vietnamese").open_restaurant()
Restaurant("Pho Hut", "Vietnamese").describe_restaurant()

