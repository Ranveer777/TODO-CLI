import sys
from datetime import date
from Commands import addTodo, getTodos, deleteTodo, completed


def main():

    if len(sys.argv) == 1:                                                #Prints help when no additional args are provided
        print("""Usage :-
$ ./todo add "todo item"  # Add a new todo
$ ./todo ls               # Show remaining todos
$ ./todo del NUMBER       # Delete a todo
$ ./todo done NUMBER      # Complete a todo
$ ./todo help             # Show usage
$ ./todo report           # Statistics""")
    
    else:
        command = sys.argv[1]
        todofile = 'todo.txt'
        donefile = 'done.txt'

        try:
            with open(todofile, 'r') as file: 
                pass
            with open(donefile, 'r') as file:
                pass
        
        except FileNotFoundError:
            with open(todofile, 'w') as file: 
                pass
            with open(donefile, 'w') as file:
                pass

        if command == 'add':                                              #Add Todo  
            print(addTodo.add_todo(sys.argv))

        elif command == 'ls':                                             #List all todos 
            getTodos.get_todos() 

        elif command == 'help':                                           #Prints Usage
            print("""Usage :-
$ ./todo add "todo item"  # Add a new todo
$ ./todo ls               # Show remaining todos
$ ./todo del NUMBER       # Delete a todo
$ ./todo done NUMBER      # Complete a todo
$ ./todo help             # Show usage
$ ./todo report           # Statistics""")

        
        elif command == 'del':                                            #Delete todo
            print(deleteTodo.delete_todo(sys.argv))
        
        elif command == 'done':                                           #Mark a todo as done
            print(completed.done_todo(sys.argv))

        elif command == 'report':                                         #Reporting pending and completed todos 
            with open(todofile, 'r') as file:
                pending = len(file.readlines())

            with open(donefile, 'r') as file:
                compl = len(file.readlines())

            print("{} Pending : {} Completed : {}".format(date.today(), pending, compl))  

        else:
            print("Not a valid command")    


if __name__ == "__main__":
    main()