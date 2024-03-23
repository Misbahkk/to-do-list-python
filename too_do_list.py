tasks = []

def add_task():
    task_description = input("Enter Your task description:\n")
    tasks.append({"Description":task_description,"completed":False})
    print("Task Added")

def veiw_task():
    for i , task in enumerate(tasks):
        print(f"{i+1}. {task['Description']} - {'completed' if task['completed'] else 'Not Completed'}")

def mark_task_completed():
    if not tasks:
        print("No Task is mark is completed")
        return
    veiw_task()
    task_num = int(input("Enter a task Number:"))
    if task_num>0 and task_num<=len(tasks):
        tasks[task_num-1][ 'completed'] =True
    print("The Task is Mark as completed")

def remove_task():
    if not tasks:
        print("No Task is mark is completed")
        return
    veiw_task()
    task_num = int(input("Enter a task Number:"))
    del tasks[task_num-1]
    print("Task is Remove succensfully")

while True:
    print("===To Do List ===")
    print("1. Add Task")
    print("2. View Task")
    print("3. Mark Task as completed")
    print("4. Task Delete")

    choise = int(input("Enter your choise: "))
    if choise == 1:
        add_task()
    elif choise == 2:
        veiw_task()
    elif choise == 3:
        mark_task_completed()
    elif choise == 4:
        remove_task()
    else:
        print("Invalid Choise")
        break
    

    

