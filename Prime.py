for hello in range(10):
    print ("Hello!")
    
for i in range (15):
    i=i+1
    print ("Hello! i is set to " + str(i))

# This will give you the sum for all the number between 1 and 1M
for sume6 in range (1):
    sum =100000000 * (1000000+1)/2
    print("sum is equal to "+ str(sum))

# Put 2 inputs and it'll give you the power of 2 for each one
integer1 =input("please enter an integer between 1 and 10: ")
integer1 = int(integer1)
integer2 =input("please enter another integer between 1 and 10: ")
integer2 = int(integer2)
for number in range (integer1, integer2, 2):
    print (number**2)

# Prime Numbers
integrity = int(input("Please enter an integer: "))
if integrity == 2:
     print ("prime number")
elif integrity %2 == 0:
    print ("even number. not prime number.")
elif integrity <=1:
    print("not a prime number")
else:
    print("not prime number")