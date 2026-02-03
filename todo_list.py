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
        status = input("Select task status (Not Started, In Progress, Complete): ").lower()
        if status in valid_status:
            break
        else:
            print("Invalid selection. Please try again.")

    task_item = {
        "task" : task,
        "description" : description,
        "category" : category,
        "priority" : priority,
        "due date" : due_date,
        "status" : status
    }

    tasks.append(task_item)
    print(f'{task} added.')

#-----------------------------------------------------------------------
#   option [2] view all tasks
#-----------------------------------------------------------------------

def view_tasks():
    print("Displaying All Tasks")
    print(tabulate(tasks, headers="keys", tablefmt="fancy_grid"))

#-----------------------------------------------------------------------
#   option [3] view by priority
#-----------------------------------------------------------------------

def view_priority():
    # re order list to group by priority high to low. may need to numerate where high = 3 or something like that.
    numbered_tasks_list = []
    for task in tasks:
        if task["priority"] == "high":
            task_priority = 1
        elif task["priority"] == "medium":
            task_priority = 2
        else:
            task_priority = 3 

        numbered_tasks_dict = {
            "priority number" : task_priority,
            "task" : task["task"],
            "description" : task["description"],
            "category" : task["category"],
            "priority" : task["priority"],
            "due date" : task["due date"],
            "status" : task["status"]
        }

        numbered_tasks_list.append(numbered_tasks_dict)

    #sort list by priorities
    sorted_list = sorted(numbered_tasks_list, key=lambda item: item["priority number"])

    # remove priority number
    numberless_task_list = []
    for task_item in sorted_list:
        tasks_dict = {            
            "task" : task_item["task"],
            "description" : task_item["description"],
            "category" : task_item["category"],
            "priority" : task_item["priority"],
            "due date" : task_item["due date"],
            "status" : task_item["status"]
        }

        numberless_task_list.append(tasks_dict)

    print(tabulate(numberless_task_list,headers = "keys", tablefmt="grid"))

#-----------------------------------------------------------------------
#   option [4] view by status
#-----------------------------------------------------------------------

def view_status():    
    while True:
        search_term = input("Enter status to view (Not Started, In Progress, Complete): ").lower()
        if search_term in valid_status:
            break
        else:
            print("Invalid Category. Please try again.")
    
    searched_list = []
    for task in tasks:
        if search_term == task['status']:
            searched_list.append(task)
        
    print(tabulate(searched_list,headers = "keys", tablefmt="grid"))

#-----------------------------------------------------------------------
#    display numbered list to choose from
#-----------------------------------------------------------------------
def create_numbered_list():
    print('Displaying All Tasks')
    numbered_list = []    
    for number, task_item in enumerate(tasks, start=1):
            numbered_task = {
            "number": number,
            "task" : task_item["task"],
            "description" : task_item["description"],
            "category" : task_item["category"],
            "priority" : task_item["priority"],
            "due date" : task_item["due date"],
            "status" : task_item["status"]
            }                
            numbered_list.append(numbered_task)

    print(tabulate(numbered_list,headers = "keys", tablefmt="grid"))
#-----------------------------------------------------------------------
#   option [5] Mark complete
#-----------------------------------------------------------------------

def mark_complete():
    # display numbered list to choose from.
    create_numbered_list()    

    # user chooses task # to mark complete.
    while True:
        try:
            choice = int(input("Select task to mark complete: "))
            if 1 <= choice and choice <= len(tasks):
                break
            else:
                print("Number out of range. Please try again.")

        except ValueError:
            print("Invalid entry. Please try again.")

            
    # choice-1 is index for global tasks list that we want to mark complete.
    selected_task = tasks[choice-1]
    selected_task['status'] = 'complete' 
    print(f'({selected_task["task"]}) task marked completed.')
        
    print(tabulate(tasks,headers = "keys", tablefmt="grid"))

    #-----------------------------------------------------------------------
#   option [6] delete contact
#-----------------------------------------------------------------------

def delete_contact():
    # show all tasks
    view_tasks()



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
        write_json()    
    elif option == '6':
        delete_contact()
        write_json()     

    else:
        print("Invalid action. Please try again.")

