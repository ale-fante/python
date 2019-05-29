with open("digits.txt") as file_object:
	contents = file_object.read()
	print(contents)

	print("OR LINE BY LINE:")

with open("digits.txt") as file_object:
	for line in file_object:
		print(line.rstrip())
		print(len(line.rstrip()))



