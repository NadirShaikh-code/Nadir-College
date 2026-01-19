#Nadir shaikh
#UIN- 251P086
print("Nadir Shaikh")
print("UIN-251P086")
task_list=[

    ("Task 1","2025-02-06","High"),
    ("Task 2","2025-02-07","Medium"),
    ("Task 3","2025-02-08","Low"),
]
print("Initial Task List:")
print(task_list)
new_task = ("Task 4","2025-02-09","High")
task_list.remove(task_list[1])
print(task_list)
task_list.sort()
print(task_list)

print("\n Updated Task list:" )
print(task_list)