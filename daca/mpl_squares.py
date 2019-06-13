import matplotlib.pyplot as plt
import numpy as np
import csv

with open('Country_Of_Birth.csv', 'r') as nationality:
	nationality = csv.reader(nationality)

	for line in nationality:
		#print(line[0])
		int(line[2])
		print(line)