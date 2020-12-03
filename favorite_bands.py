#Ryan Walters Dec2 2020 -- A simple program of a few of my favorite bands using everything that I learned in Chapter 3 of the No Starch Python book

#Initial list
favorite_bands = ['gorillaz', 'nujabes', 'queens of the stone age', 'hall & oats', 'lotus', 'black sabbath']

#Capitalizing the list with a method found on Stack Overflow
favorite_bands = [bands.title() for bands in favorite_bands]
print("Some of my favorite bands are", ', '.join(favorite_bands[0:-1]), f"and {favorite_bands[-1]}.")

#Adding values
favorite_bands.append('the prodigy')
favorite_bands.append('thievery corporation')
favorite_bands = [bands.title() for bands in favorite_bands]
print(f"\nI also forgot about two of my other favorites. {favorite_bands[-2]} and {favorite_bands[-1]}")

#Inserting values
print("\nThere's a few metal bands I really like that I forgot to include. I will add them to the full list.")
favorite_bands.insert(2, 'mastodon')
favorite_bands.insert(5, 'lamb of god')
favorite_bands.insert(7, 'power trip')
favorite_bands.insert(4, 'iron maiden')
favorite_bands = [bands.title() for bands in favorite_bands]
print("\nThe current working list of my favorite bands is:", ', '.join(favorite_bands[0:-1]), f"and {favorite_bands[-1]}")

#Removing items from a list
print("\nThis list is too long. I'm going to remove a few bands.")

#END OF PROGRAM
