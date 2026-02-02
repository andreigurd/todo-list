import json
from tabulate import tabulate
from datetime import datetime,date,timedelta

valid_priority = ['high', 'medium', 'low']
valid_status = ['not started', 'in progress', 'complete']
valid_category = ["work", "personal", "shopping"]

#-----------------------------------------------------------------------
#   opening tasks json file
#-----------------------------------------------------------------------
try:
    with open('tasks.json', 'r') as file:
        tasks = json.load(file)
except FileNotFoundError:
    print("Tasks file not found. Blank list created.")
    tasks = [] # makes an empty list
except json.JSONDecodeError:
    print("Issue loading Tasks file. File empty or invalid JSON file. Blank Tasks list created.")
    tasks = []
except ValueError:
    print("Invalid Tasks item. Blank list created.")
    tasks = []
except PermissionError:
    print("Need permission to access Tasks file. Blank Tasks list created.")
    tasks = []


#-----------------------------------------------------------------------
#   showing menu
#-----------------------------------------------------------------------

def show_menu():    
    print("[0] Exit")
    print("[1] Add task")
    print("[2] View all tasks")
    print("[3] View by priority")
    print("[4] View by status")
    print("[5] Mark complete")
    print("[6] Delete task")   


#-----------------------------------------------------------------------
#   option [1] Add task
#-----------------------------------------------------------------------

def add_task():
    # Each task should have:
# Description
# Priority (High, Medium, Low)
# Due date
# Status (Not Started, In Progress, Complete)

    while True:
        try:
            task = str(input("Enter task: ").lower())
            if task == "":
                print("Blank is invalid entry. Please try again.")
            else:
                break                
        except ValueError:
            print("Invalid entry. Please try again.")

    while True:
        try:
            description = str(input("Enter task description: ").lower())
            if description == "":
                print("Blank is invalid entry. Please try again.")
            else:
                break                
        except ValueError:
            print("Invalid entry. Please try again.")

    while True:        
        category = input("Enter category (Work, Personal, Shopping): ").lower()
        if category in valid_category:
            break
        else:
            print("Invalid Category. Please try again.")

    while True:        
        priority = input("Select task priority (High, Medium, Low): ").lower()
        if priority in valid_priority:
            break
        else:
            print("Invalid selection. Please try again.")

    while True:
        try:
            due_date = str(input("Enter task due date in (yyyy-mm-dd) format: ").lower())
            if due_date == "":
                print("Blank is invalid entry. Please try again.")
            else:
                break                
        except ValueError:
            print("Invalid entry. Please try again.")

    while True:        
        status = input("Select task priority (Not Started, In Progress, Complete): ").lower()
        if status in valid_status:
            break
        else:
            print("Invalid selection. Please try again.")


#-----------------------------------------------------------------------
#   function to write to tasks json
#-----------------------------------------------------------------------
def write_json():
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file, indent=4)
        

#-----------------------------------------------------------------------
#   while loop to get user input
#-----------------------------------------------------------------------

while True:
    show_menu()
    option = input("\nSelect Option: ")
    if option == '0':        
        write_json()
        print("Goodbye.")
        break    
    elif option == '1':
        add_task()
        write_json()
    elif option == '2':
        view_tasks()
    elif option == '3': 
        view_priority()
    elif option == '4': 
        view_status()
    elif option == '5': 
        mark_complete()    
    elif option == '6':
        delete_contact()
        write_json     

    else:
        print("Invalid action. Please try again.")

