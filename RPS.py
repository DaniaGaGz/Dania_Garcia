import random
print("Let's play Rock Paper Scissors")

options = ["rock","paper","scissors"]


while True: 
    userch = input ("Type one of the options: ")
    compch = random.choice(options)
    print (compch)
    if userch == "quit":
        print(f"Thank you for playing. My guess was {compch}. Goodbye")
        break
    if userch == "":
        print (f"Option required. My guess was {compch}")
        continue
    if userch == compch:
        print("tie")
    elif((userch == "rock" and compch == "scissors") or (userch == "scissors"and compch == "paper") or (userch == "paper" and compch == "rock")):
        print("You win!")
    else: 
        print("You lose :(")