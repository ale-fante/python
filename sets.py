# A set is a collection which is unordered and unindexed.
# In Python sets are written with curly brackets.

thisset = {"apple", "banana", "cherry"}
print(thisset)

# You cannot access items in a set by referring to an index,
# since sets are unordered the items has no index.

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)


thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

# Once a set is created, you cannot change its items, but you can add new items.

thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

# Combines both
thisset = {"apple", "banana", "cherry"}
thisset.update(["orange", "mango", "grapes"])
print(thisset)

thisset = {"apple", "banana", "cherry"}
print(len(thisset))

thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)


# Remove the last item
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

# Empties the set
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

# Deletes set
thisset = {"apple", "banana", "cherry"}
del thisset

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

""" Python functions available for sets"""

# Add
# Usage: set.add(element)
# elment - Required. The element to add to the set

fruits = {"apple", "banana", "cherry"}
fruits.add("orange") 
print(fruits)

thisset = {"apple", "banana", "cherry"}
thisset.add("apple")
print(thisset)

# Remove
# Usage: set.clear()

fruits = {"apple", "banana", "cherry"}
fruits.clear()
print(fruits)


# Copy
# Usage: set.copy()

fruits = {"apple", "banana", "cherry"}
x = fruits.copy()
print(x)


# difference - returns a set that contains the difference between two sets
#  Usage: set.difference(set)
# parameter - the set to check for differences in

x = {"apple", "banana", "cherry", "google"}
y = {"google", "microsoft", "apple", "cherry"}
print("Set with items that only exist in set x, and not in set y:")
z = x.difference(y) 

print(z)


# Return a set that contains the items that only exist in set y, and not in set x:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = y.difference(x) 
print("Set with items that only exist in set y, and not in set x:")
x = {"apple", "banana", "cherry"}
print(z)

# Remove the items that exist in both sets:
# difference_update()
# Usage: The difference_update() method is different from the difference() method, 
# because the difference() method returns a new set, without the unwanted items, 
# and the difference_update() method removes the unwanted items from the original set.

# set.difference_update(set)
# set	Required. The set to check for differences in

x = {"apple", "banana", "cherry", "google", "amazon"}
y = {"google", "microsoft", "apple", "google"}

x.difference_update(y) 

print(x)
#set(['amazon', 'cherry', 'banana'])


# The discard() method removes the specified item from the set.

# This method is different from the remove() method, because the remove() method will raise an error
# if the specified item does not exist, and the discard() method will not.
# USAGE: set.discard(value)
# value	Required. The item to search for, and remove

fruits = {"apple", "banana", "cherry"}
fruits.discard("banana") 
print(fruits)


sisters = {"Ale", "ricky", "cris"}
sisters.discard("ricky")
print("Removed non-syblings:")
print(sisters)

sisters = {"Ale"}
sisters.discard("Ale")
print(sisters) # doesn't throw an error if empty

# intersection
# Return a set that contains the items that exist in both set x, and set y:

x = {"cris", "ale", "edi"}
y = {"ale", "martha", "henry"}

z = x.intersection(y) 

print(z)
# The intersection() method returns a set that contains the similarity between two or more sets.

# Usage: set.intersection(set1, set2 ... etc)


x = {"ale", "barb", "cris"}
y = {"cris", "dee", "enriq"}
z = {"fer", "gaby", "cris"}

result = x.intersection(y, z)
print("Compare 3 sets, and return a set with items that is present in all 3 sets:")
print(result)

#intersection_update()
# Syntax: set.intersection_update(set1, set2 ... etc)
x = {"Cris", "edi", "Ale"}
y = {"Cris", "Ale", "Ricky"}

x.intersection_update(y) 
print("Remove the item that is not present in both x and y")
print(x)


x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}

x.intersection_update(y, z)
print("Compare the 3 sets and return a set with items that is present in all sets")
print(x)

# isdisjoint()
# syntax: set.isdisjoint(set)
# The isdisjoint() method returns True if none of the items are present in both sets, otherwise it returns False.
x = {"ale", "cris", "edi"}
y = {"Ted", "ricky", "pollo"}
z = x.isdisjoint(y) 
print("Return True if no items in set x are present in set Y:")
print(z)


x = {"ale", "cris", "edi"}
y = {"ale", "ricky", "pollo"}
z = x.isdisjoint(y) 
print("Return false if one or more items are present in both sets:")
print(z)



























