# A tuple is a collection which is ordered and unchangeable.
# In Python tuples are written with round brackets.

thistuple = ("apple", "banana", "cherry")
print(thistuple)

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

# Once a tuple is created, you cannot change its values. Tuples are unchangeable.

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

thistuple = ("apple", "banana", "cherry")
if "orange" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
else:
  print("Nope, not here")

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

thistuple = ("apple", "banana", "cherry")
del thistuple
print("Tuple deleted!")

# the tuple() constructor can be used to make a  tuple
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

# return the number of times the value 5 appears in the tuple

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5, 5, 5, 5, 5)
x = thistuple.count(5)
print(x)

# usage: tuple.count(value)
# parameter: value - required. The item to search for

# Search for the first occurrence of the value 8 and return its index
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.index(8)
print(x)

# usage: tuple.index(value)
# parameter: value - required. The item to search for

fruits = {"apple", "banana", "cherry", "watermelon"}
more_fruits = ["orange", "mango", "grapes", "pears"]
fruits.update(more_fruits)

print fruits

