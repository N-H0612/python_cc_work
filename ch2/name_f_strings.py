'''
Here we will have two variables with values assigned to them, and our third variable full_name will be constructed using the first two
variables we declare. Ususally I just would join them as the following 
full_name = first_name + " " + last_name

However, this chapter introduces using f-strings to use a variable within another variable. Something I see when using ReGex methods. 
maybe in time, this would be beneficial, so I'll give it a shot. 

Note: f-strings were first introduced in 3.6, if using 3.5 or earlier you would need to use format() method
'''
#my ususal way
first_name = "nicole"
last_name = "herrera"
full_name = first_name + " " + last_name + ", my ususal way"
print(full_name)

#f-strings way
full_name = f"{first_name} {last_name}"
print("The f-string way:")
print("\t" + full_name)

#f-strings can be used to compose messages using the info asociated with the var
full_name = f"{first_name} {last_name}"
print(f"Hi! {full_name.title()}, we are using the f-string way to make this message!")

#f-string can be used to construct the message, but then assign that message to a var
full_name = f"{first_name} {last_name}"
message = f"Hi! {full_name.title()}, we are using the f-string way to make this message, assign it to a var message, and then printing that message!"
print(message)

#using the format() method to construct full_name var
full_name = "{} {}".format(first_name, last_name)
#using the full_name var we constructed above with f-string below! now we are getting crazy!
print(f"Hi {full_name.title()}, we are using the format method() & f-strings!")
