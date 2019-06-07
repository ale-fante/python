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








