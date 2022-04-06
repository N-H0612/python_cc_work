#underscores can be used make big integers easier to read, and python will still interpret it as numerical 
#100,000
big_number = 100_000
print(big_number)

#if you divide any two numbers, even if they are integers, it will always result in a float 
#a float is any number with a decimal point 
#5000.0
print(big_number/2)

#if you mix an integer and float in any operation you will always get a float 
#200000.0
print(big_number * 2.0)

#just like uipath has multi assign so does python! and you can do it with numbers or strings
x, y, z = 1, 2, 3 
print(x)
print(y)
print(z)

x, y, z = "a", "b", "c"
print(x)
print(y)
print(z)

#You can mix and match too!
x, y, z = "a", 1, "b"
print(x)
print(y)
print(z)

#You can even do operations! 
x, y, z = "b"+"c", 1 + 2, 3
print(x)
print(y)
print(z)

#Constant variables that are never meant to change are ususally capitalize 
MAX_LIFE_COUNT = 100
