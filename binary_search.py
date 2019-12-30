
def binary_search(list, item):
  # Low and high keep track of which part of the list you'll search in.
  low = 0
  high = len(list) -1

  # While you have not narroed it down to an element, check the middle element.
  while low <= high:
    mid = (low + high)
    guess = list[mid]
    if guess == item:
      return mid
    if guess > item:
      high = mid -1
    else:
      low = mid + 1
  return None
  
my_list = [0,1,2,3,12,19,30,55,100]

# Return the index in which the number is
print binary_search(my_list, 3)
print binary_search(my_list, 1)
print binary_search(my_list, 2)
print binary_search(my_list, 55)
print binary_search(my_list, 100)
print binary_search(my_list, -1)
