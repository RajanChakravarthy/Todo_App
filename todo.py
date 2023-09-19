import functions
import time

now = time.asctime()
print(f'It is {now}')


while True:
    user_input = input('Type show, add, edit, delete or exit: ')
    user_input = user_input.strip()
    # Show action
    if user_input.startswith('show'):

        todos = functions.get_todo()

        for i,item in enumerate(todos):
            print((f'{i+1}. {item}').title(),end='')

    # Add action
    elif user_input.startswith('add'):
        todo = user_input[4:]+ '\n'
        todos = functions.get_todo('todos.txt')

        todos.append(todo)

        functions.write_todos(todos)

    # Edit Action
    elif user_input.startswith('edit'):
        try:
            todos = functions.get_todo()

            index_number = int(user_input[5:])
            old_todo = todos[index_number-1]
            new_todo = input('Whats the updated todo? ')
            todos[index_number-1] = new_todo + '\n'
            print('The to-do list has been updated.')

            functions.write_todos(todos)

        except ValueError:
            print('Enter the index number of the todo to be edited.')
            continue

        except IndexError:
            print('Entered index number does not exist.')
            continue

    # delete Action
    elif user_input.startswith('delete'):
        try:
            todos = functions.get_todo()

            # code to delete a item from the todo list
            index_to_delete = int(user_input[7:])
            removed_todo = todos.pop(index_to_delete-1).strip('\n')
            print(f"The item '{removed_todo}' has been removed from the list. ")

            functions.write_todos(todos)

        except IndexError:
            print('Entered index number does not exist.')
            continue

        except ValueError:
            print('Enter the index number of the todo to be edited.')
            continue

    # Exit action
    elif user_input.startswith('exit'):
        print('The program exited.')
        break

    else:
        print('The command does not exist. Enter a proper command.')

print('bye')