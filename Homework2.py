enterNewTask = 1
taskStatus = 2
removeTaskByName = 3
remarkTaskAsDone = 4
searchTaskValue = 5
exitProgram = 6

#ID_Name Full # ofir kalanthroff_322290651
print("Welcome to the Task Manager!")
running = True # keep the program returning on itself
toDoList = [] # the list of the thing that i return
while running: # the loop of the program that true while running is true
    print("Choose an option:\n    1. Add task\n    2. Show tasks\n    3. Remove task\n    4. Mark task as done\n    5. Count tasks with keyword\n    6. Exit")
    option = input("Your choice: ")
    if not option.isdigit():
        print("Invalid input. Please enter a number. ")
        continue
    option = int(option)
    if not 1 <= option <= 6:
        print("Invalid choice. Please choose a number from 1 to 6 . ")
        continue

    if option == enterNewTask: # first option
        toDoList.append([input("Enter new task: "), False])
        print("Task added .")
    elif option == taskStatus: #second option
        if len(toDoList) == 0:
            print("No tasks found. ")
        i = 0
        while i < len(toDoList): # insert the value the user wants
            taskName, taskStatus = toDoList[i]
            statusString = ""

            if taskStatus: #if its done
                statusString = "[V]"
            else: # if not done
                statusString = "[]"
            print(str(i+1) + ". " + taskName + " " + statusString)
            i += 1
    elif option == removeTaskByName:
        removeTask = input("Enter task name to remove :")
        i = 0
        currentRemoveId = -1 #value that doesnt exist
        while i < len(toDoList): #searching the value to remove
            taskName, taskStatus = toDoList[i]
            if taskName == removeTask:
                currentRemoveId = i
                break
            i += 1
        if currentRemoveId != -1: #if i found the value
            toDoList.pop(currentRemoveId)
            print("Task removed.")
        else: #if i didnt found the value
            print("Task not found .")
    elif option == remarkTaskAsDone:
        taskId = input("Enter task number to mark as done: ")
        if not taskId.isdigit():
            print("Invalid input. Please enter a number. ")
            continue
        taskId = int(taskId)
        if not 1 <= taskId <= len(toDoList):
            print("Invalid task number .")
            continue
        toDoList[taskId - 1][1] = True
        print("Task marked as done.")
    elif option == searchTaskValue:
        keyword = input("Enter keyword :")
        i = 0
        counter = 0
        while i < len(toDoList):
            if keyword.upper() in toDoList[i][0].upper().split():
                counter += 1
            i += 1
        print("Found", counter, "tasks with" , keyword)
    elif option == exitProgram:
        print("Goodbye!")
        running = False

