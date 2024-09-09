import random
# List of words to choose from
input('guess my word: ')
# Initialize the user's guess
user_guess = ""

while True:
    word_list = ['python', 'java', 'javascript', 'ruby', 'html', 'css']
    # Randomly select a word from the list
    selected_word = random.choice(word_list)
    print(selected_word)

    if selected_word == 'quit':
        print('thank you for playing')
        break 

    if selected_word == word_list:
        print('youve guessed it!') 
        
    
    