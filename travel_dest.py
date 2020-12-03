#Ryan Walters Nov 21 2020 -- Practicing the different sorting methods with travel destinations

#Initial list
travel_dest = ['tokyo', 'venice', 'amsterdam', 'osaka', 'wales', 'dublin']

#Printing as a raw Python list and then in order
print(travel_dest)
print(sorted(travel_dest))

#Printing in reverse alphabetical order without a permanent change to the list
print(travel_dest)
print(sorted(travel_dest, reverse=True))

#Using reverse method to change the order and then back again
print(travel_dest)
travel_dest.reverse()
print(travel_dest)
travel_dest.reverse()
print(travel_dest)

#Alphabetical sorting and reverse permanent
travel_dest.sort()
print(travel_dest)
travel_dest.sort(reverse=True)
print(travel_dest)

#END OF PROGRAM
