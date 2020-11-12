#Ryan Walters Nov 11 2020 -- modifying items in a list

#Initial motorcycle list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

#Changing 0 index
motorcycles[0] = 'ducati'
print(motorcycles)

#Adding honda back using the append method
motorcycles.append('honda')
print(motorcycles)

#Starting with an empty list and using .append to reassign the values
motorcycles = []
motorcycles.append('yamaha')
motorcycles.append('suzuki')
motorcycles.append('honda')
print(motorcycles)

#Inserting a new value at a given index
motorcycles.insert(0, 'ducati')
print(motorcycles)

#Removing an item from the list using a .del statement
del motorcycles[3]
print(motorcycles)

#Removing an item but keeping its value using the pop() method
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

#Using the pop() method to demonstrate chronological order in a string
motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print(f"The last motorcycle that I bought was a brand new {last_owned.title()}.")

#Using the pop() method on a specific index
motorcycles = ['honda', 'yamaha', 'suzuki']
second_owned = motorcycles.pop(1)
print(f"The second motorcycle I ever owned was a real sleek {second_owned.title()}.")

#Removing a specific item using the remove() method
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"I never did own a {too_expensive.title()}, though. Those bastards are way too expensive.")