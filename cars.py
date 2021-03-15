#Ryan Walters Nov 21 2020 -- Learning the different sorting methods with a simple list of car companies

#Initial list
cars = ['mazda', 'lincoln', 'lexus', 'volvo', 'toyota']
print("The initial list:")
print(cars)

#Sort alphabetically
print("\nThe list sorted in alphabetical order "
    "(original list cannot be called):")
cars.sort()
print(cars)

#Sorting reverse alphabetically
print("\nThe list sorted in reverse alphabetical order "
    "(original list cannot be called):")
cars.sort(reverse=True)
print(cars)

#Resetting the list for the purposes of the sorted() exercise
cars = ['mazda', 'lincoln', 'lexus', 'volvo', 'toyota']
print("\nThe original list (reset):")
print(cars)

print("\nThe newly sorted list (use sorted() so the "
    "original list can be called):")
print(sorted(cars))

print("\nThe original list again:")
print(cars)

#Printing the list in reverse order
print("\nThe list in reverse order (permanent):")
cars.reverse()
print(cars)

#Finding the length of the list
length = len(cars)
print(f"\nThe length of the list is {length}.")

#END OF PROGRAM
