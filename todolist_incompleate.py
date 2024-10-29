# A simple to-do list manager for high school students using functions and list comprehension

# Initial to-do list
todo_list = ["Math homework", "Science project", "Read history book", "Practice piano"]

# Function to display the current to-do list
def display_todo_list():
    for item in todo_list:
        print (item + "\n")
    #TODO display the list

# Function to add a new task
def add_task():
    task = input("Want to add a new task? ")
    todo_list.append(task)
    #TODO the user wants to add a task. 
    display_todo_list()

# Function to remove a task by its name
def remove_task():
    removy = input ("Want to remove a task? ")
    if removy in todo_list:
        todo_list.remove(removy)
    else:
        print("Not found")
    #TODO 
    display_todo_list()

# Function to find the index of a task
def find_task():
    find = input("Enter your task: ")
    print(find.index(find))

    #The user wants to know in what position is a task. 

# Function to complete and remove the first task
def complete_task():
    del todo_list[0]

    #The user wants to remove the first task. 

# Function to filter tasks containing a specific keyword using list comprehension
def filter_tasks():
    #TODO create a list comprehension variable to filter tasks containing a specific keyword
    keyword = input("enter keyword:")
    filtering = [task if keyword in task else "not found" for task in todo_list ]


        
            
# Main menu to choose options
def main():
    
    while True:
        print("\nTo-Do List Manager Menu")
        print("1. View To-Do List")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Find Task")
        print("5. Complete First Task")
        print("6. Filter Tasks by Keyword")
        print("7. Exit")
        


        choice = input("Menu: ")

        if choice == "7":
            print ("You've exited.")
            break 
        elif choice == "1":
            display_todo_list()
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            find_task()
        elif choice  == "5":
            complete_task()
        elif choice == "6":
            filter_tasks()
       
        
main()

        #TODO create the if staments for the user. 
        

# Run the main function