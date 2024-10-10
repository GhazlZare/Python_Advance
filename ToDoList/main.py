from Manager import *

def main():
    manager = Manager()
    while True:
        print('''What do you want to do?
            1. Add Task
            2. Mark Task as Done
            3. View All Tasks
            4. View Task Summary
            5. Exit''')
        choice = input("please enter the number of the function you want to do: ")
        if choice == "1" :
            task_id = input("Enter Task ID (numeric): ")
            title = input("Enter Task Title: ")
            description = input("Enter Task Description: ")
            try: 
                task = manager.creat_task(title, description, task_id)
                manager.add_task(task)
            except ValueError as e:
                print(e)
        elif choice == "2" :
            task_id = input("Enter the task id (numeric) that you want to mark as done: ")
            manager.mark_done(task_id)
        elif choice == "3" :
            manager.display_tasks()
        elif choice == "4" :
            manager.summary()
        elif choice == "5" :
            break
        elif choice == "" :
            continue
        else:
            print("Out of range")

if __name__ == "__main__":
    main()