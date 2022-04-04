'''
This section will focus on how to format strings such as , white spaces, new lines, etc to make it easier on the eyes. 
It will also discuss apostrophes.
'''

#Adding tabs append \t infront of any string 
print("\tThis line is tabbed to the right.")
print("\t\tThis line is double tabbed to the right.")
print("\t\t\tThis line is triple tabbed!")

#Adding new line append \n infront of any string 
print("Nicole's interests:\nVideogames\nFood\nReality Shows\nCoffee")

#Combining new lines and tabs \n\t
print("Nicole's interests:\n\tVideogames\n\tFood\n\tReality Shows\n\tCoffee")

'''
Stripping whitespace is important when having to do string comparsion. 
'''

favorite_language = 'python '
print(f"{favorite_language}whitespaces?")

#rstrip() method trims the right side of all whitespace
print(f"{favorite_language.rstrip()}whitespaces?")


left_whtspace = ' python'
print(f"{left_whtspace}")

#lstrip() method trims the left side of all whitespace
print(f"{favorite_language.lstrip()}")

whtspace_right_left = ' python '
print(f"{whtspace_right_left}whitespace on both sides of ' python '")

#strip() method trims both sides of all whitespace
print(f"{whtspace_right_left.strip()}whitespace stripped from both sides of 'python'")

'''
appostrophes: using single apostrophe within single quotes will cause errors
ex: 'This will sentence's apostrophe will cause an error'

'''

message = "This will sentence's apostrophe will not cause an error"
print(message)
