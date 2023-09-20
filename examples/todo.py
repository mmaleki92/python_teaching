tasks = []

while True:
    print("Enter '1' to add task")
    print("Enter '2' to delete task")
    print("Enter '3' to view tasks")
    print("Enter '4' to exit")

    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added.")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks to delete.")
        else:
            for i, task in enumerate(tasks):
                print(f"{i}: {task}")
            index = int(input("Enter task number to delete: "))
            del tasks[index]
            print("Task deleted.")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks.")
        else:
            for i, task in enumerate(tasks):
                print(f"{i}: {task}")

    elif choice == "4":
        break

    else:
        print("Invalid choice.")
