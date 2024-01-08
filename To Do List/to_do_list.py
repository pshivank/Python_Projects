def addTask(tasks,task_name):                          # created function to add tasks in our list 
    tasks.append(task_name)
    print('Added Successfully....')                    # showing message to user after task is added 
    return tasks

def showTasks(tasks):                                  # created function for showing task to user 
    if len(tasks) != 0 :
        for s in range(len(tasks)):
            print(s+1 , '.',tasks[s])
    else:
        print('Sorry ! No task available.')
        
    print()
        
def markCompleted(completed_tasks ,tasks,task_name):      # function for marking completed tasks
    if len(tasks) != 0 and task_name in tasks :
        completed_tasks.append(task_name)
        tasks.remove(task_name)
        print('Marked Completed And Moved To Completed Tasks ...')
        
    else:
        print('No task Available or all tasks are completed..')
        
    print()
    
    
def deleteTask(tasks,task_name):                                        # function for deleting tasks
    if len(tasks) == 0 :
        print('No task available..')
    
    elif task_name in tasks:
        tasks.remove(task_name)
        print('Deleted Successfully .... ')
        
    print()

def main():
    tasks = []
    completed_tasks = []
    while True:
        try:                                                              # showing available options to users 
            print(""" ---  Available Choices  --- 
            1. Add Task 
            2. Show Tasks
            3. Completed Tasks
            4. Mark Completed
            5. Delete Task
            6. Quit """)
            print()

            choice = int(input('Enter Your Choice :--- '))              # taking input to know what user wants to perform 
            print()

            if choice == 1 :
                addTask(tasks,input('Enter task name :--- '))
                print()

            elif choice == 2:
                showTasks(tasks)
                print()

            elif choice == 3 :
                if len(completed_tasks) != 0:
                    for s in range(len(completed_tasks)):
                        print(s+1 , '.',completed_tasks[s])

                else:
                    print('All tasks are incomplete...please complete your tasks...') 
                print()


            elif choice == 4 :
                markCompleted(completed_tasks,tasks,input('Enter task name to mark complete : -- '))
                print()

            elif choice == 5 :
                deleteTask(tasks,input('Enter task name :---- '))
                print()

            elif choice == 6 :
                print(' Quited.......')
                break
                
            else:
                print('Please Choose from options only..')
                print()
                
                
        except ValueError:
            print('Invalid Input.....')                                 # excepting error if user enters invalid input
            
        
if __name__ == '__main__':
    main()