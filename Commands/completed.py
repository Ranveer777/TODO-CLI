from datetime import date

def done_todo(arg):
    todofile = './todo.txt'
    donefile = './done.txt'
    try:
        num = int(arg[2])  
        with open(todofile, "r") as file:
            lines = file.readlines()

        if num <= len(lines) and num >= 1:
            curr_date = date.today()
            with open(donefile, 'a') as file:
                file.write("{}-{}-{} ".format(curr_date.year, curr_date.month, curr_date.day) + lines[num - 1])

            with open(todofile, "w") as file:
                for line in lines:
                    if line != lines[num - 1]:
                        file.write(line)
            return "Marked todo #{} as done.".format(num)

        else:
            return "Error: todo #{} does not exist.".format(num)

    except IndexError:
        return "Error: Missing NUMBER for marking todo as done."