import sys

while True:
	print('Type exit to exit')
	response = input()
	response = str(response)
	if response == 'exit':
		sys.exit()
	print('You typed ' + response + '.')
