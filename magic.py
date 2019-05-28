magicians = ['alice', 'david', 'carolina']

for magician in magicians:
	print(magician.title() + ", that was a great trick!")

print("I can't wait to see your trick, " + magician.title() + ".\n")

# *********************************************************

numbers = list(range(1, 6))
print("PRINT FROM 1 TO 5")
print(numbers)

# *********************************************************

squares = []
for value in range(1, 11):
	square = value**2
	squares.append(square)

print("Print all the squares")
print(squares)

# *********************************************************

squares = []
for value in range(1,11):
	squares.append(value**2)

print("Print squares only within the range of 1 and 11")
print(squares)

# *********************************************************

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0]

print("Minimum")
print(min(digits))

print("Maximum")
print(max(digits))

print("Sum of all digits")
print(sum(digits))

# *********************************************************

# Count for twenty

one_to_twenty = []
for num in range(1,21):
	one_to_twenty.append(num)

print(one_to_twenty)

# *********************************************************

# Cube comprehension - Use a list comprehension to generate
# a list of the first 10 cubes.

cubes = []
for value in range(0,10):
	cubes.append(value**3)

print("Print the first three cubes")
print(cubes)

# *********************************************************

players = ["Charles", "martina", "michael", "florence", "eli"]

print("Here are the first three players on my team: ")
for player in players[:3]:
	print(player.title())

# *********************************************************

my_foods = ["pizza", "falafel", "carrot"]
friend_food = my_foods[:]
my_foods.append("cannoli")
friend_food.append("ice cream")

print("My favorite foods are: ")
print(my_foods)

# *********************************************************

dimensions = (200, 50)

print("Original dimensions: ")
for dimension in dimensions:

	print(dimension)

