def delete_todo(arg):
    todofile = './todo.txt'
    try:
        num = int(arg[2])
        with open(todofile, "r") as file:
            lines = file.readlines()

        if num <= len(lines) and num >= 1:
            with open(todofile, "w") as file:
                for line in lines:
                    if line != lines[num - 1]:
                        file.write(line)
            return "Deleted todo #{}".format(num)            
        else:
            return "Error: todo #{} does not exist. Nothing deleted.".format(num)                
    
    except IndexError:
        return "Error: Missing NUMBER for deleting todo."