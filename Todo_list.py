""" This is a basic To-Do list created using python.I allows users to 
1.Add tasks
2.View Tasks
3.Remove tasks
"""

todo_list=[]

while True:
  print("\n TODO LIST MENU")
  print("\n1. Add Task")
  print("\n2.View Tasks")
  print("\n3.Remove task")
  print("\n4.Exit")

  choice = input("Enter your choice")

  if choice=="1":
    task=input("Enter the task ")
    todo_list.append(task)
    print("task added")

  if choice=="2":
    print("\n YOUR TASKS...")
    if len(todo_list)==0:
      print("No tasks yet")
    else:
      for i, task in enumerate(todo_list,start=1):
        print(f"{i}.{task}")

  elif choice=="3":
    print("\n Your Tasks..")
    for i, task in enumerate(todo_list,start=1):
        print(f"{i}.{task}")
    task_no=int(input("Enter the taskno to remove "))
    if 1 <= task_no <= len(todo_list):
      removed=todo_list.pop(task_no-1)
      print(f"removed: {removed}")
    else:
      print("Invalid task number")

  elif choice=="4":
    print("EXITING...")
    break

else:
    print("Invalid choice!!")
