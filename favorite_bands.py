#Ryan Walters Dec2 2020 -- A program with a list of a few of my favorite bands using everything that I learned in Chapter 3 of the No Starch Python book

#Initial list
favorite_bands = ['gorillaz', 'nujabes', 'queens of the stone age', 'hall & oats', 'lotus', 'black sabbath', 'pink floyd']

#Capitalizing the list with a method found on Stack Overflow
favorite_bands = [bands.title() for bands in favorite_bands]
print("Some of my favorite bands are", ', '.join(favorite_bands[0:-1])+", " f"and {favorite_bands[-1]}.")

#Adding values
favorite_bands.append('the prodigy')
favorite_bands.append('thievery corporation')
favorite_bands = [bands.title() for bands in favorite_bands]
print(f"\nI also forgot about two of my other favorites: {favorite_bands[-2]} and {favorite_bands[-1]}")

#Inserting values
print("\nThere's a few metal bands I really like that I forgot to include. I will add them to the full list by using the insert() method on various index positions.")
favorite_bands.insert(2, 'mastodon')
favorite_bands.insert(5, 'lamb of god')
favorite_bands.insert(7, 'power trip')
favorite_bands.insert(4, 'iron maiden')
favorite_bands = [bands.title() for bands in favorite_bands]
print("\nThe current working list of my favorite bands is:", ', '.join(favorite_bands[0:-1])+", " f"and {favorite_bands[-1]}")

#Removing items from a list
print("\nThis list is too long. I'm going to remove Queens of the Stone Age.")
del favorite_bands[3]
print("\n Without the band I removed, the current working list is", ', '.join(favorite_bands[0:-1])+", " f"and {favorite_bands[-1]}")
del_nujabes = favorite_bands.pop(1)
del_sabbath = favorite_bands.pop(7)
del_prodigy = favorite_bands.pop(8)
print(f"\nI also only want the bands that are currently active in my list, so I am going to remove {del_nujabes}, {del_sabbath}, and {del_prodigy}. I used the pop() method so that I could print them in this string.")
print(f"\nThe lead singer of my favorite thrash metal band, {favorite_bands[6]}, recenetly passed away. I hope that they remain active, but I am going to remove them from the list for now. I will remove this band from the list by its value.")
remove_powertrip = 'Power Trip'
favorite_bands.remove(remove_powertrip)
#NOTE: Once title case is established it must be respected in future applications of the string when assigning values.
print("\nHere is the current working list of my faovite bands:", ", ".join(favorite_bands[0:-1])+", " f"and {favorite_bands[-1]}. Next, I will sort them alphabetically.")

#Sorting the list alphabetically (temporary)
sorted_bands = sorted(favorite_bands)
print("\nIn alphabetical order, my current working list of favorite bands is:", ", ".join(sorted_bands[0:-1])+", " f"and {sorted_bands[-1]}")
sorted_reverse = sorted(favorite_bands, reverse=True)
print("\nIn reverse alphabetical order, my current working list of favorite bands is:", ", ".join(sorted_reverse[0:-1])+", " f"and {sorted_reverse[-1]}")
print("\nHowever, because I used the sorted() method, I can still print the list in its original form like so:", ", ".join(favorite_bands[0:-1])+", " f"and {favorite_bands[-1]}.")

#Sorting the list alphabetically (permanent)
favorite_bands.sort()
print("\nI am now using a different sorting method to list these bands in alphabetical order, but it is permanent:", ", ".join(favorite_bands[0:-1])+", " f"and {favorite_bands[-1]}.")

#Sorting in reverse order
favorite_bands.reverse()
print("\nThe reverse method allows me to print the list in reverse order:", ', '.join(favorite_bands[0:-1])+", " f"and {favorite_bands[-1]}")
favorite_bands.reverse()
print("\nI can use the same method to revert back to the previous order like so:", ', '.join(favorite_bands[0:-1])+", " f"and {favorite_bands[-1]}.")

#Length
print("\nAnd finally, even though it would be easy to count in this case, the length of my list of favorite bands is", str(len(favorite_bands))+".")

#END OF PROGRAM
