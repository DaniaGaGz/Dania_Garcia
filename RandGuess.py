import random
guess = input("guess a number between 1 and 10 (or type 'quit' to exit): ")
# Check if the guess is within the valid range
ran = str(random.randint(1, 10))

while True:
    
    if guess == 'quit':
        print("The number was " + ran + " Thanks for playing")
        break     
        
    elif guess == ran:
        print("Congratulations")
            
    elif int(guess) > int(ran):
        print("Too high")
            

    elif int(guess) < int(ran):
        print ("Too low")
            

    else:
        print ("please stay within the range")
    guess = input("Try Again: ")