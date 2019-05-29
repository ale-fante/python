requested_toppings = ["mushrooms", "extra cheese", "pepperoni"]

if "mushrooms" in requested_toppings:
	print("Adding Mushrooms")

if "pepperoni" in requested_toppings:
	print("Adding pepperoni")

if "extra cheese" in requested_toppings:
	print("Adding extra cheese")

print("\nFinished making your pizza!")

# * ---------------------------------------

alien_0 = {"x_position": 0, "y_position": 25, "speed": "medium"}

print("Original x-position: " + str(alien_0["x_position"]))

# Move the alien to the right
# Determine how far to move the alien based on its current speed

if alien_0["speed"] == "slow":
	x_increment = 1

elif alien_0["speed"] == "medium":
	x_increment = 2

elif alien_0["speed"] == "high":
	x_increment = 3

else:
	x_increment = 5


alien_0["x_position"] = alien_0["x_position"] + x_increment

print("New x-position: " + str(alien_0["x_position"]))

# * ---------------------------------------

# Loop through a dictionary

favorite_languages = {
	"Ale": "python",
	"Rick": "ruby",
	"Alex": "Java",
	"Ashley": "C#",
}

friends = ["Ale", "Ashley"]
for name in favorite_languages.keys():
	print(name.title())

	if name in friends:
		print("Hi " + name.title() + ", I see your favorite languages is " +
		favorite_languages[name].title() + "!")


