'''
To-Do List
'''

def todo():
    tasks = []
    while True:
        print ("--- TO DO LIST ---")
        print ("(1) ~ Add Task")
        print ("(2) ~ Remove Task")
        print ("(3) ~ View Tasks")
        print ("(4) ~ Exit")
        
        choice = input ("Enter your choice from (1-4): ")

        if choice == "1":
            add = (input("Enter the task to add: "))
            tasks.append(add)
            print ("Task added.")
        elif choice == "2":
            taskr = (input("Enter the task to be removed: "))
            try:
                tasks.remove(taskr)
                print("Task removed.")
            except:
                print("There's no such Task!")
        elif choice == "3":
            print("--- TASK LIST ---")
            for task in tasks:
                print(f"{task}")
        elif choice == "4":
            print ("Have a productive day ahead!")
            break 
        else:
            print ("Invalid Choice!")
    
todo()
