def get_todos():
    todofile = './todo.txt'
    try:
        with open(todofile, 'r') as file:
            lines = file.readlines()

        num_of_lines = len(lines)
        if num_of_lines > 0:
            for i in range(num_of_lines - 1, -1, -1):        
                line = lines[i].strip('\n')
                print("[{0}] {1}".format(i + 1, line))
        else:
            print("There are no pending todos!")
    except BaseException:
        print("There are no pending todos!")