user_choice = 0
tasks = []


#function that allows us to see all tasks
def show_tasks():
    task_index = 0
    for task in tasks:
        print(task + " [" + str(task_index) + "]")
        task_index += 1


#function that allows us to add  new task
def add_task():
    task = input("Add task name: ")
    tasks.append(task)
    print("Add Task!")


#function that allows us to delete task
def delete_task():
    task_index = int(input("Choose index to delete file: "))

    if task_index < 0 or task_index > len(tasks) - 1:
        print("Task with this index does not exist")
        return
    tasks.pop(task_index)
    print("Task was deleted!")


#function that allows us to save task to the txt file
def save_tasks_to_file():
    file = open("tasks.txt","w")
    for task in tasks:
        file.write(task+"\n")
    file.close()


#function that allows us to load task's from txt file
def load_tasks_from_file():
    try:
        file = open("tasks.txt")

        for line in file.readlines():
            tasks.append(line.strip())

        file.close()
    except FileNotFoundError:
        return


load_tasks_from_file()


#until user choice is != 5, print 5 options
while user_choice != 5:
    print("\n1. Show tasks")
    print("2. Add task")
    print("3. Delete task")
    print("4. Save changes in file")
    print("5. Quit")

    user_choice = int(input("\nChoose number: "))

    if user_choice == 1:
        show_tasks()

    if user_choice == 2:
        add_task()

    if user_choice == 3:
        delete_task()

    if user_choice == 4:
        save_tasks_to_file()

    if user_choice <= 0 or user_choice > 5:
        print("Choose correct number")
