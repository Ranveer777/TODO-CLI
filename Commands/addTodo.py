def add_todo(arg):
    todofile = './todo.txt'
    try:
        value = arg[2]
        with open(todofile, 'a') as file: 
            file.write(value + '\n')

        return 'Added todo: "{}"'.format(value)    
    except IndexError:
        return "Error: Missing todo string. Nothing added!"