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

class Battery():

	""" A simple attempt to model a battery for an electric car."""

	def __init__(self, battery_size=60):
		"""Initialize the battery's attributes"""
		self.battery_size = battery_size


	def describe_battery(self):
		"""Print a statement describing the battery size"""
		print("This car has a " + str(self.battery_size) + "-kWh battery.")

	def get_range(self):
		"""Print a statement about the range this battery provides"""
	    if self.battery_size == 70:
	        range = 240
	    elif self.battery_size == 85:
	        range = 270
	    else: 
	         # chose a fitting value for 60 - or better: use a formular to calc range  
	         # so you do not have to provide hardcoded range values for all charges
	         # between 0 and 2000
	        range = 200 # or smth like: range = self.battery_size // 3

	"""Find way to pull in the correct value for str(range)"""
	message = "This car can go approximately " + str(range) + " miles on a full charge."
	print(message)

class ElectricCar(Car):

	def __init__(self, make, model, year):
		super().__init__(make, model, year)
		self.battery = Battery()
