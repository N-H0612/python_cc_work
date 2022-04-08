#first item in a list starts at the index of 0
videogames = ["Pokemon", "Animal Crossing", "Mario 3D World", "Xenoblade"]
print(f"videogames is a list var that has the following items in it: {videogames}")
#videogames[0] will give us Pokemon
print(videogames[0])

#You can get the last item in a list by using -1 as the index
#videogames[-1] will give us Xenoblade
print(videogames[-1])
# using -2 will give us the second last item of the list, -3 third last item, and so forth
print(videogames[-3])

#You can use f-strings with items in a list
message = f'My favorite video game of all time has always been "{videogames[0].upper()}"!'

print("\n" + message)

#We can change the value of any item in a list by setting that item's position to another value
videogames[-1] = "Mortal Kombat"
print(videogames)

#To add to a list we use the following method append() with the item in the brackets
# lists can items of any type ex we added a number to the list that had all str items
videogames.append(9000)
print(videogames)

#Unlike append() that adds the item to the end of the list, you can use the insert() method to insert an item at a specific index
#for fun we add a list obj at the second place in the list
videogames.insert(1, ["Sims"])
print(videogames)

#We can remove items from a list using the del statement. You will need to know the index of the item that you want to delete
del videogames[1]
del videogames[-1]
print(videogames)

#We can pop out the last item of a list and store it in var for use later, using the method pop()
popped_videogame = videogames.pop()
print(popped_videogame)

print(f"The last videogame I bought was {popped_videogame.title()}.")
print(videogames)

#You can also pop out items from a specific location in a list. To do so, we need to put the index within the ()
second_videogame = videogames.pop(1)
print(f"The second game I bought was {second_videogame.title()}")

#Everytime you use pop, you are removing items, so you will now see that our videogames list is smaller!
print(videogames)

#We also can remove an item from a list if we know the value we wish to remove. 
#use the remove() method. In the brackets place the value you wish to remove
gave_away = "Mario 3D World"
print(f"I gave away {gave_away} to my friend")
videogames.remove(gave_away)
print(videogames)

'''
Organization of Lists
'''
candys = ["M&Ms", "Snickers", "Hersey", "Reeses"]
#sorting a list A-Z permanently with sort() method. Leave the brackets empthy
candys.sort()
print(candys)


