def factorial(n):
    resultoffactorial = 1
    for i in range (2,n + 1):
        resultoffactorial *= i
    print(resultoffactorial)
        

factorial(6)
factorial(11)
factorial(15)
factorial(22)

def remainder(a,b):
    print('Your result is: ')
    print(a-((a//b)*b))

remainder(3,2)
remainder(21,4)
remainder(131,19)
remainder(81,9)