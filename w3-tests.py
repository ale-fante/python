

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
# print("Ingresa tu nombre:")
# nombre = input()
# print("Hola, ", nombre)

# --------------------------------------------------

c = 5
c += 3
print("cinco += 3 es igual a 5 mas 3, que es " + str(c))

f = 5
f -= 3
print("five -= 3 is the same as five minus three, which equals to  " + str(f))

d = 2
d *= 3
print("Dos *= 3 es igual a 2 por 3, que es " + str(d))

s = 9
s /= 3
print("Two /= 3 is the same as 9 divided by 3, which equals to " + str(s))


m = 5
m%=3
print("Five %= 3 is the same as 5 divided by three, which equals to " + str(m))

x = 9
x//=3
print("9 //= 3 equals to: " + str(x))

exp = 5
exp **= 3
print("Five to the power of three is: " + str(exp))

# ----------------------------------------------------
# LOGICAL OPERATORS

a = 5
print(not(a > 3 and a < 10))

b = 15
print(b > 3 or b < 4)

x = 5
print(x > 3 and x < 10)

x = ["apple", "banana"]
print("banana" in x)

x = ["apple", "banana"]
print("pineapple" not in x)



