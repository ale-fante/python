

# Get the thrid character through the 4th
b = "Hello, World!"
print(b[2:5])

# Remove whitespace from beginnign and end
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

# Returns length of a string
a = "Alejandra!"
print(len(a))

# All to lower case
a = "ALEjandra LEDesmA"
print(a.lower())

# All to upper case
a = "zAcatECAs"
print(a.upper())

# replace a character or string with another
a = "I am happy"
print(a.replace("happy", "sad"))

# Split into substrings
a = "Lista, de, palabras, divididas, por las, comas"
print(a.split(",")) #['Lista', ' de', ' palabras', ' divididas', ' por las', ' comas']

# Enter data and save it into variable "x"
print("Ingresa tu nombre:")
nombre = input()
print("Hola, ", nombre)