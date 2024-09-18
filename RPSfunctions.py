import random
def choice(txt):
    print(f'**********{txt}**********')
options = ["rock","paper","scissors"]


while True: 
    print("Let's play Rock Paper Scissors")
    userch = input ("Type one of the options: ")
    compch = random.choice(options)
    print (compch)
    if userch == "quit":
        choice("goodbye")
        break
    if userch not in options:
        choice('not allowed. not in options')
        continue
    if userch == compch:
        choice("tie")
    elif((userch == "rock" and compch == "scissors") or (userch == "scissors"and compch == "paper") or (userch == "paper" and compch == "rock")):
        choice("You win!")
    else: 
        choice("You lose :(")