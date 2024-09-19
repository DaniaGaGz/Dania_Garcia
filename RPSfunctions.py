import random
def choice(txt):
    print(f'**********{txt}**********')
options = ["rock","paper","scissors"]


while True: 
    print("Let's play Rock Paper Scissors")
    userch = input ("""Type one of the options, 1 for "rock", 2 for "paper", 3 for "scissors": """)
    compch = random.choice(options)
    print (compch)
    if userch == "quit":
        choice("goodbye")
        break
    if userch.isnumeric() and userch.isdigit():
        userch = int(userch) -1
        if userch not in range(1,3):
            choice('not allowed. not in options')
            continue
    #if userch not in options:
        #choice('not allowed. not in options')
        #continue
        
    if options[userch] == compch:
        choice("tie")
    elif((options[userch] == "rock"  and compch == "scissors")or (options[userch] == "scissors"and compch == "paper") or (options[userch] == "paper" and compch == "rock")):
        choice("You win!")
    else: 
        choice("You lose :(")