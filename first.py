
#code shows year one would clock 100 years with age inputted
age = int(input("Enter your age: "))
oldage = 100 - age
oldyear = 2019 + oldage
#print ("you would be 100 years")
print ("In " + str(oldyear) + ", you would be 100 years.")


#code that explains if a number entered is odd or even
N = int(input("Enter a number: "))
even = N % 2
if even == 0:
    print ("The number " + str(N) + " is divisible by 2 therefore it is an even number.")
elif even != 0:
    print ("The number " + str(N) + " is not divisible by 2 therefore it is an odd number.")
