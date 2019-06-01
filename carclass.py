class Car():
	""" A simple attem pte to represent a car"""

	def __init__(self, make, model, year):
		"""Initialize attributes to describe a car"""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		"""Return a neatly formatted descriptive name."""
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model

		return long_name.title()

	def read_odometer(self):
		"""Print a statement showing the car's mileage."""
		print("This car has " + str(self.odometer_reading) + " miles on it.")

	def update_odometer(self, mileage):
		"""Set the odometer reading to a given value. Reject the change if it rolls odometer back"""
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll the odometer back!")

	def increment_odometer(self, miles):
		"""Add given amout to the odometer reading."""
		self.odometer_reading += miles

my_new_car = Car('Honda', 'Accord', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 1020
my_new_car.read_odometer()
