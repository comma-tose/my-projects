# Comments are rushed as this is a simple cleanup of an old assignment

# Add a task
def add_task(tasks):
    global todo
    todo.append(tasks)

# Remove a task
def remove_task(tasks):
    global todo
    todo.pop(tasks - 1)

# Display tasks
def display_tasks():
    for i in range(len(todo)):
        print(f"{i+1}: {todo[i]}")

# Save list
def save_to_file(path):
    global todo
    with open(path, "w") as file:
        for item in todo:
            file.write(f"{item}\n")

# Load list
def load_from_file(path):
    global todo
    todo = []
    try:
        with open(path, 'r') as file:
            for line in file:
                todo.append(line.strip())
    except FileNotFoundError:
        print("No file to load from.")

todo = []

# Prompt to load a list on launch
if input("Import a previous list? (y/n)\n>>> ").lower() == "y":
    load_from_file("todo.txt")
else:
    print("Not importing file.")

# Main menu
while True:
    print("-- To-Do List Menu --")
    print("1. Add a task")
    print("2. Remove a task")
    print("3. Print the task list")
    print("4. Save the task list to a file")
    print("5. Read a task list from a file")
    print("6. Exit")
    choice = str(input("What would you like to do?\n>>> "))
    if choice == "1":
        add_task(str(input("Enter the task to add:\n>>> ")))
    elif choice == "2":
        try:
            remove_task(int(input("Enter the task number to remove:\n>>> ")))
        except ValueError:
            print("You entered something that isn't a number. Cancelling...")
    elif choice == "3":
        display_tasks()
    elif choice == "4":
        save_to_file("todo.txt")
    elif choice == "5":
        if str(input("You are about to override your list. Continue? (y/n)\n>>> ")).lower() == "y":
            load_from_file("todo.txt")
        else:
            print("Cancelling...")
    elif choice == "6":
        if str(input("You are about to exit. If you haven't saved your list, it will be lost. Continue? (y/n)\n>>> ")).lower() == "y":
            print("Goodbye!")
            exit()
        else:
            print("Cancelling...")
    else:
        print("Invalid option!")