first_name= input("What's your first name? ")
last_name= input("What's your last name?")

longstr = len(first_name + last_name)

initias = first_name[0] + last_name[0]

double_fname = ""
for letter in first_name:
    double_fname += letter + letter

reversed_name = last_name[::-1]
print(reversed_name)
print(f"Hello {last_name}, {first_name}! Your name has {longstr} letters, and your initials are {initias}. {double_fname}, your name spelled backwards is {reversed_name}.")