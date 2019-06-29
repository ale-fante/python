time = int(raw_input("Enter the elapsed time in seconds: " + '\033[1m'));
print("\n"+ "\033[0m" + "The elapsed time in seconds = " + str(time));

time = time % (24 * 3600);
hour = time / 3600;

time = time % 3600;
minutes = time / 60;
9
time = time % 60;
seconds = time;

print("\n" + "The equivalent time in hours:minutes:seconds = " + "%d:%d:%d" % (hour, minutes, seconds));
