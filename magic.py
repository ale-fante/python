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


