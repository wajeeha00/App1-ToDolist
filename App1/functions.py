import os 

def get_todos(file_path="todos.txt"):
    if not os.path.exists('todos.txt'):
        with open('todos.txt','w') as file:
            pass
    """ Returns a list of todos from a file """
    with open(file_path, "r") as file:
        todos = file.readlines()
    for i in range(len(todos)):
        todos[i] = todos[i][:-1]
    return todos

def write_todos(todos,file_path="todos.txt"):
    """ Writes a list of todos to a file """
    with open(file_path, "w") as file:
        for todo in todos:
            file.write(f"{todo}\n")

def enumeration(todos):
    for idx,todo in enumerate(todos):
        print(f"{idx+1}. {todo}")
