#code shows how a new list of even numbers is derived from old list

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
even = []
for a in a:
    if a % 2 == 0:
        even.append(a)
#print without indentation shows the answers at once
#while print with indentation shows answers one by one in the loop
print (even)
    
    


