from functions import get_todos, write_todos, enumeration
import datetime
import time
def main():
    while True:
        user_action = input("add, show, edit,complete or exit: ").strip().lower()

        if user_action.startswith("add") or "new" in user_action:
            todo = user_action[4:].strip()
            todos = get_todos()
            todos.append(todo)
            write_todos(todos)
            
        elif user_action.startswith("show") :

            todos = get_todos()
            for index,items in enumerate(todos):
                print(f"{index+1}. {items}")
        
        elif user_action.startswith("edit"):
            todos = get_todos()
            try:
                inp = int(user_action[5:]) -1 
                if inp > len(todos):
                    raise IndexError
                todos[inp] = input("Enter the new todo: ").strip()
                write_todos(todos)
            
            except IndexError:
                print("Invalid index")
            
            except ValueError:
                print("Invalid input")
            
        elif user_action.startswith("complete"):
            todos = get_todos()
            index = int(user_action[9:]) -1
            try:
                todos.pop(index)
                write_todos(todos)
            except IndexError:
                print("Invalid index")
            
            except ValueError:
                print("Invalid input")
        elif user_action.startswith("exit"):
            exit("bye")
        else:
            print("Invalid action")
    
if __name__ == "__main__":
    print(f"It is {time.strftime('%A, %d %B %Y %H:%M:%S')}")
    print(f"### YOUR TO DO LIST  ###")
    todos = get_todos()
    enumeration(todos)
    main()
