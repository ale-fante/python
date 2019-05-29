filename = "programming.txt"

with open(filename, 'w') as file_object:
  file_object.write("1.\n")
  file_object.write("2.\n")
  file_object.write("3.\n")
  file_object.write("4.\n")
  file_object.write("5.\n")
  file_object.write("6.\n")
  file_object.write("7.\n")
  file_object.write("8.\n")
  file_object.write("9.\n")
  file_object.write("10.\n")


test_text = input ("Enter a number: ")

# Converts the string into a integer. If you need
# to convert the user input into decimal format,
# the float() function is used instead of int()
test_number = int(test_text)

# Prints in the console the variable as requested
print ("The number you entered is: ", test_number)
