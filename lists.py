# List is a collection which is ordered and changeable. Allows duplicate members.

# Print list
thislist = ["apple", "banana", "cherry"]
print(thislist)

# Access item on index # 2
thislist = ["apple", "banana", "cherry"]
print(thislist[2])

# Add item on index # 1
thislist = ["apple", "banana", "cherry"]
thislist[1] = "coconut"
print(thislist)

# Loop through the list and print all items
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

# Check if an item is in the list
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")


# Determine how many items are in the list
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

# Add an item to the end of the list
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
thislist.append("coconut")
thislist.append("mango")
print(thislist)

# Add item to specific index
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "coconut")
print(thislist)
thislist.insert(1, "mango")
print(thislist)

# Remove specified item
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# or
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# Copy a list
thislist = ["apple", "banana", "cherry"]
my_fruits_copy = thislist[:]
print(my_fruits_copy)

# or
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

# weird way of making a list
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

# Sort lists alphabetically
cars = ['Ford', 'BMW', 'Volvo']
cars.sort()
print("Sort lists alphabetically")
print cars

# Sort ascending
cars = ['Ford', 'BMW', 'Volvo']
cars.sort(reverse=True)
print("Sort ascending")
print cars

# Sort by length of value
def myFunc(e):
  return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

cars.sort(key=myFunc)
print ("Sort by length of value")
print cars

def myFunc(e):
  return e['year']

# Sort based on year value
cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]

cars.sort(key=myFunc)
print("Sort based on year value")
print cars

# Sort based on length of value and reversed
# A function that returns the length of the value:
def myFunc(e):
  return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

cars.sort(reverse=True, key=myFunc)

print("Sort based on length of value and reversed")
print cars


# Reverse order of list
fruits = ['apple', 'banana', 'cherry']

fruits.reverse()
print("Reverse the oder of fruits:")
print fruits

# Add element
fruits = ['apple', 'banana', 'cherry']
print("Normal list:")
print fruits
x = fruits.pop(1)
print("Popped element:")
print x
print("updated list:")
print fruits

# Insert the value "orange" as the second element of the fruit list
# list.insert(pos, elmnt)
fruits = ['apple', 'banana', 'cherry']
print("Insert the value 'orange' as the second element of the fruit list:")
fruits.insert(1, "orange")
print fruits

# Return index of item 32

fruits = [4, 55, 64, 32, 16, 32]
x = fruits.index(32)
print x

fruits = ['apple', 'banana', 'cherry']
x = fruits.index("cherry")
print x

# Add elements of cars to fruits
fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)
print fruits

# Return the number of times a value appears in the list
fruits = ['apple', 'banana', 'cherry', 'c', 'c']
x = fruits.count("c")
print x

# Append to list
a = ["apple", "banana", "cherry"]
b = ["Ford", "BMW", "Volvo"]
a.append(b)
print a

# Append
fruits = ['apple', 'banana', 'cherry']
fruits.append("orange")

print fruits



