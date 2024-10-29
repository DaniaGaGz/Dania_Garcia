# Initial list of students
#TODO: Create a List of Students names. Add 10 names. Name this list as 'student'
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

    #TODO HINT: Print each student in the 'students' list
def display_students():
    for i in nombres:
        print(i)
    print("\n")
    
    lin = len(nombres)
    print(f"Current students: {lin}")
    print(f"_____________________________________") 


# Add a new student to the list
def add_student(fname, lname):
    #TODO HINT: Ask the user for the student's name.
    fullname = fname + " " + lname
    #TODO Append the student's name to the 'students' list
    nombres.append(fullname)
    #TODO display the updated list
    display_students()
    #! After complete the function remove 'pass'

# Remove a student from the list by name
def remove_student():
    #TODO HINT: Ask the user for the student's name to removeD
    removy = input("Remove a name: ")
    #TODO Check if the student is in the list, then remove it
    if removy in nombres:
        nombres.remove(removy)
    #TODO If the student is not found, print an error message
    else:
        print("Error. Student not found.")
    #TODO display the updated list
    display_students()
    #! After complete the function remove 'pass'

# remove a student from the end of the list
def pop_student():
    #TODO HINT: Remove the last student from the list
    #TODO If the list is not empty, display the name of the student removed
    if nombres != "":
        poped_name = (nombres[-1])
        nombres.pop()
        print(f"Student Removed: {poped_name}")
        display_students()
    #TODO If the list is empty, print a message saying there are no students left
    else:
        print("Error.This list is empty.")
    #TODO display the updated list
    display_students
    #! After complete the function remove 'pass'

# Update a student's name in the list
def update_student():
    #TODO HINT: ask for the current name of the student
    wrong_name = input("Current name: ")
    #TODO Check if the student is in the list, then ask for the new name
    if wrong_name in nombres: 
        newname = input(f"Your current name is {wrong_name}, what do you want to change it to? (type here): ")
        index_to_update = nombres.index(wrong_name)
        nombres[index_to_update] = newname
        #TODO Update the student's name in the list
        display_students()
    #TODO If the student is not found, print an error message
    else:
        print(f"Error.{wrong_name} not found in list")
    #TODO display the updated list
    display_students()
    #! After complete the function remove 'pass'

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

        #TODO depending of the user choice option (1 - 5), call the correct function
        display_students()
        if choice == "1":
            firstName = input("First name")
            LastName = input("last NAme")
            add_student(firstName, LastName)
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

#menu()