todo_list = [] # Global List တစ်ခု၊ Dictionary တွေကို သိမ်းဖို့
next_id = 1    # Task ID တွေကို auto-increment လုပ်ဖို့

def add_task(task_name):
    """Adds a new task to the to-do list."""
    global next_id # Global variable ဖြစ်တဲ့ next_id ကို ပြင်ဆင်နိုင်ဖို့
    task = {
        "id": next_id,
        "task": task_name,
        "completed": False
    }
    todo_list.append(task)
    next_id += 1
    print(f"Task '{task_name}' added with ID: {task['id']}")

def view_tasks():
    """Displays all tasks in the to-do list."""
    if not todo_list: # List ထဲမှာ ဘာမှမရှိရင်
        print("Your to-do list is empty.")
        return

    print("\n--- YOUR TO-DO LIST ---")
    for task in todo_list:
        status = "✅" if task["completed"] else "⏳" # Emoji လေးတွေနဲ့ status ပြခြင်း
        print(f"ID: {task['id']} | Status: {status} | Task: {task['task']}")
    print("-----------------------")

def mark_completed(task_id):
    """Marks a task as completed given its ID."""
    found = False
    for task in todo_list:
        if task["id"] == task_id:
            task["completed"] = True
            print(f"Task ID {task_id} marked as completed.")
            found = True
            break
    if not found:
        print(f"Task with ID {task_id} not found.")

def delete_task(task_id):
    """Deletes a task from the list given its ID."""
    global todo_list # Global variable ကို ပြင်ဆင်နိုင်ဖို့
    original_len = len(todo_list)
    # Task ID ကိုက်ညီတာကို ဖယ်ရှား
    todo_list = [task for task in todo_list if task["id"] != task_id]
    
    if len(todo_list) < original_len:
        print(f"Task with ID {task_id} deleted.")
    else:
        print(f"Task with ID {task_id} not found.")

def display_menu():
    """Displays the main menu options to the user."""
    print("\n--- TO-DO LIST MENU ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")
    print("-----------------------")

# Main program loop
def run_todo_app():
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            task_name = input("Enter task description: ")
            if task_name: # Task name အလွတ်မဖြစ်စေရန် စစ်ဆေး
                add_task(task_name)
            else:
                print("Task description cannot be empty.")
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            try:
                task_id = int(input("Enter ID of task to mark as completed: "))
                mark_completed(task_id)
            except ValueError:
                print("Invalid input. Please enter a number for Task ID.")
        elif choice == '4':
            try:
                task_id = int(input("Enter ID of task to delete: "))
                delete_task(task_id)
            except ValueError:
                print("Invalid input. Please enter a number for Task ID.")
        elif choice == '5':
            print("Exiting To-Do List Application. Goodbye!")
            break # Loop ကနေ ထွက်ပြီး Program ကို ရပ်
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

# Program စတင် run ရန်
if __name__ == "__main__":
    run_todo_app()
