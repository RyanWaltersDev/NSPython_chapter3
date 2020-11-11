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