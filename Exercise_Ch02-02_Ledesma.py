

firstName = raw_input(" Enter your first name: " + '\033[1m');
studyHours = float(raw_input('\033[0m'+ " Enter your expected study hours on Saturday: "  + '\033[1m'));

print str('\033[0m' + "\n"+ " Hello, " + firstName + "!" + "\n" +  " On Saturday, you need to study " + str(3 * studyHours)
		 + " hours for the exam.");