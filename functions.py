def get_todo(filepath='todos.txt'):
    ''' This function returns the list of todos from the txt file. '''
    with open(filepath, mode='r') as file:
        todos = file.readlines()
    return todos

def write_todos(todos_local, filepath='todos.txt'):
    ''' The function writes the todo list into the todos.txt file. '''
    with open(filepath, mode='w') as file:
        file.writelines(todos_local)