# Initial list of students
nombres = [
    "Axel",
    "Nala",
    "Zara",
    "Leo",
    "Sienna",
    "Kai",
    "Luna",
    "Orion",
    "Juno",
    "Riven"
]

#Print each student in the 'students' list
def display_students():
    for i in nombres:
        print(i)
    print("\n")
    
    lin = len(nombres)
    print(f"Current students: {lin}")
    print(f"_____________________________________") 


# Add a new student to the list
def add_student():
    namey = input("Add a name: ")
    nombres.append(namey)
    display_students()

# Remove a student from the list by name
def remove_student():
    removy = input("Remove a name: ")
    
    if removy in nombres:
        nombres.remove(removy)
    else:
        print("Error. Student not found.")
    display_students()

# remove a student from the end of the list
def pop_student():
    if nombres != "":
        poped_name = (nombres[-1])
        nombres.pop()
        print(f"Student Removed: {poped_name}")
        display_students()
    else:
        print("Error.This list is empty.")
    display_students


# Update a student's name in the list
def update_student():
    wrong_name = input("Current name: ")

    if wrong_name in nombres: 
        newname = input(f"Your current name is {wrong_name}, what do you want to change it to? (type here): ")
        index_to_update = nombres.index(wrong_name)
        nombres[index_to_update] = newname
        display_students()
    else:
        print(f"Error.{wrong_name} not found in list")
    display_students()


# Menu to manage student operations
def menu():
    while True:
        print("\nMenu:")
        print("1. Add a student")
        print("2. Remove a student")
        print("3. Pop a student")
        print("4. Update a student's name")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        
        if choice == "1":
            add_student()
        elif choice == "2":
            remove_student()
        elif choice == "3":
            pop_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            print("See you next time!")
            break

# Start the program
menu()
