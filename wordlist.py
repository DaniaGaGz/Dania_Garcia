import random
# List of words to choose from

# Initialize the user's guess
word_list = ['python', 'java', 'javascript', 'ruby', 'html', 'css']

while True:

    user_guess = input('guess my word: ')
    # Randomly select a word from the list
    selected_word = random.choice(word_list)
    print(selected_word)

    if selected_word == 'quit':
        print('thank you for playing')
        break 

    if (user_guess == selected_word):
        print('''you've guessed it!''') 
        break
        
    else: 
        print('''you've got it wrong''')
    
    