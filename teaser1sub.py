#Using dict function to convert two lists into a dictionary
name = ['Ayo', 'Barbie', 'Carla', 'Dede', 'Eugene']
Age = [21, 13, 57, 43, 2]

print ("\nThis code converts two lists: Name and Age into a dictionary.")
print ("Name= ", name)
print ("Age= ", Age)

d = dict(zip(name, Age))
print ("\nNames of people with their respective ages=\n ", d)

