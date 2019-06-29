firstName = raw_input("Enter your first name: " + '\033[1m');
payRate = raw_input('\033[0m' + "Enter your pay rate per hour: " + '\033[1m');
hoursWorked = raw_input('\033[0m' + "Enter the number of hours you worked last week: " + '\033[1m');

payRate = float(payRate);
hoursWorked = float(hoursWorked);

salary_calc = payRate * hoursWorked;
firstName = str(firstName);
salary = str(salary_calc);

payRate = str(payRate);
hoursWorked = str(hoursWorked);

print('\033[0m' +"\n")

print str("First Name: " + firstName);
print str("Pay Rate: $" + payRate);
print str("Hours Worked: " + hoursWorked);
print str("Salary: $" + salary);