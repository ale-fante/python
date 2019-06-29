# Write Python statements that declare the following variables: num1, num2, num3, and average.
num1 = float(125);
num2 = float(28);
num3 = float(-25);

sum_of_ints = num1 + num2 + num3
divisor = float(3);
calculate_average =  sum_of_ints / divisor;
average_to_float = float(format(calculate_average, '.2f'));
# Store 125 into num1, 28 into num2, and -25 into num3.
average = str(average_to_float);

num1 = str(125);
num2 = str(28);
num3 = str(-25);

print str("The average of " + num1 + ", " + num2 + " and " + num3 + " is " + average + ".")
print("\n")
print str("num1 is " + num1 + ".");
print("\n")
print str("num2 is " + num2 + ".");
print("\n")
print str("num3 is " + num3 + ".");
print("\n")
print str("The average of num1, num2, and num3 is " + average + ".")