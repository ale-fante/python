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
