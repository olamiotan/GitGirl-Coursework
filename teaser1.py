name = ['Ayo', 'Barbie', 'Carla', 'Dede', 'Eugene']
Age = [21, 13, 57, 43, 2]

a = tuple(name)
b = tuple(Age)
print (a)
print (b)

#method 1 - using lists
d = dict(zip(name, Age))
#print (\n)
print ("Method 1 - using lists")
print (d)

#method 2 - using tuples
f = {a[i]: b[i] for i in range(len(a))}
#print (\n)
print ("Method 2 - using tuples")
print (f)

#method 3 - using tuples
g = {k:v for k,v in zip(a,b)}
#print (\n)
print ("Method 3 - using tuples")
print (g)

#method 4 - naive method
h = {}
for i in name:
    for j in Age:
        h[i] = j
        Age.remove(j)
        break
print ("Method 4 - naive method")
print (h)
