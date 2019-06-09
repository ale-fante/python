filename = 'Sex.csv'

with open(filename) as file_object:
	lines = file_object.readlines()

pi_string = ''
for line in lines:
	pi_string += line.rstrip()
	print(line)


state_of_residence = 'State_of_residence.csv'

with open(state_of_residence) as state_of_res:
	states = state_of_res.readlines()

state_string = ''
for state in states:
	state_string += line.rstrip()
	print(state)