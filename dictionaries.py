# A dictionary is a collection which is unordered, changeable and indexed. 

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

# you can access the items of a dictionary by referring to its key name, inside square brackets
x = thisdict["model"]
print("Car Model:")
print(x)
x = thisdict.get("year")
print(x)


# Change the value of a specific item by referring to its key name
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018

print(thisdict)
print("Updated year:")
x = thisdict.get("year")
print(x)

# Loop through a dictionary
for x in thisdict:
  print("------")
  print(x)

# print all values in a dict
for x in thisdict:
  print(thisdict[x])

# use values() func to return values of dict
for x in thisdict.values():
  print(x)


# Loop throguh both keys and values
for x, y in thisdict.items():
  print(x, y)

# check if a key exists
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

# Determine how many key-value pairs a dicrionary has, use len() method
print("Value pairs in this dictionary:")
print(len(thisdict))

# Adding an item to the dictionary is done by using a new index key and assigning a value to it:
print("Add a key and value pair:")
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["Color"] = "red"
thisdict["Mileage"] = "50 K"
print(thisdict)

print("Value pairs in this dictionary:")
print(len(thisdict))

# Remove items from a dictionary using pop() with specified key name:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["Color"] = "red"
thisdict.pop("year")
print("Print dict after removed item:")
print(thisdict)

# popitem() method removes the last inserted item
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["Color"] = "red"
thisdict.popitem()
print("With Color removed:")
print(thisdict)

# del removes the item with specified key name:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

# the del word can also delete the entire dictionary
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict
# print(thisdict) #this will cause an error because "thisdict" no longer exists.

# Clear() empties the dictionary
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print("Cleared dictionary")
print(thisdict)

# You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1,
# and changes made in dict1 will automatically also be made in dict2.

# Make a copy of the dictionary
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print("Copy of dictionary:")
print(mydict)

# Make a copy of the dictionary
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print("Another copy of dictionary:")
print(mydict)

# Make another copy
thisdict =	dict(brand="Ford", model="Mustang", year=1964)
# note that keywords are not string literals
# note the use of equals rather than colon for the assignment
print(thisdict)

# Return dictionary values
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.values()

print(x)


# When a value is changed in the dictionary, the view object can also gets updated
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car["year"] = 2018
x = car.values()
print("new")
print(x)


# Insert an item to the dictionary
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.update({"color": "White"})
print("Added color")
print(car)

# Get value of the model item
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("model", "Bronco")
print("The setdefault() method returns the value of the item with the specified key.")
# USAGE: dictionary.setdefault(keyname, value)
print(x)


# Get the value of the color item, if the color item doesn't exist insert color with white
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("color", "white")
print("replace color with white")
print(x)
print(car)

# Remove the last item of the dictionary
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print("with color")
car["Color"] = "red"
print(car)
car.popitem()
print("remove last item")
print(car)

# USAGE: dictionary.popitem(keyname, defaultvalue)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print("Full dictionary------------")
print(car)
x = car.popitem()
print("remove last item:")
print(x)

# Return keys
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.keys()

print(x)

# usage dictionary.keys()

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.keys()

car["color"] = "white"

print(x)

# Create a dictionary with three keys, all with the value 0
x = ('key1', 'key2', 'key3')
y = 0

thisdict = dict.fromkeys(x, y)
print("Create a dictionary with three keys, all with the value 0")
print(thisdict)

# USAGE: dict.fromkeys(keys, value)
x = ('key1', 'key2', 'key3')

thisdict = dict.fromkeys(x)
print("Same as above without specifying the value")
print(thisdict)


