bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
#Using .title() method for a cleaner output
print(bicycles[0].title())

print(bicycles[1].title())
print(bicycles[3].title())
#Using -1 prints the last item, which in this case is the same as the 3rd index
print(bicycles[-1].title())

#Testing inserting list items into strings
message = (f"My first bicycle ever was a {bicycles[0].title()}, but my "
    f"favorite is the {bicycles[-2].title()}.")
print(message)