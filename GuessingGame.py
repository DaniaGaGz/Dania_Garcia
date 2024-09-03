print("Let's play a guessing game")
print("guess a number between 1 and 10")
guess = int(input("guess the number im thinking of "))

 

while True:
    if guess == 3:
        print("Congratulations")
        break
    elif guess > 10:
        print ("You are guessing too high")
        guess = int(input("please stay within the range 1-10 "))
        
    elif guess > 3:
        print("Too high")
        guess = int(input("Try Again: "))
    
    elif guess < 3:
        print ("Too low")
        guess = int(input("Try Again: "))