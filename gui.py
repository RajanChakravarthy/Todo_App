import functions
import PySimpleGUI as sg
import time
import os

if not os.path.exists('todos.txt'):
    with open('todos.txt', mode = 'w'):
        pass

sg.theme('BlueMono')
clock = sg.Text(time.asctime(), key='clock_key')

label_value = sg.Text('Type in a To-Do')
input_button = sg.InputText(tooltip='Enter todo.', key='todo_key')
add_button = sg.Button('Add')

list_button = sg.Listbox(functions.get_todo(),size=(50,10), key='todos_key',enable_events=True)
edit_button = sg.Button('Edit')
delete_button = sg.Button('Delete')
exit_button = sg.Button('Exit')

window = sg.Window('To-Do App',
                   layout=[[clock],
                          [label_value],
                          [input_button, add_button],
                          [list_button, edit_button, delete_button],
                          [exit_button]],
                   font= ('Arial Bold',12))

while True:
    event, value = window.read(timeout=200)
    window['clock_key'].update(time.asctime())
    match event:
        case 'Add':
            if value['todo_key'] =='':   # avoids empty task to be added.
                sg.popup('Enter the task to be added.')
            else:
                todo = value['todo_key'] + '\n'
                todos = functions.get_todo()
                todos.append(todo.title())
                functions.write_todos(todos)
                window['todos_key'].update(todos)
                window['todo_key'].update('')
        case 'Edit':
            try:
                todos = functions.get_todo()
                if value['todo_key'] =='':  # avoids replacing tasks with empty string
                    sg.popup('Enter new task to replace.')
                else:
                    todo_to_edit = value['todos_key'][0]
                    new_todo = value['todo_key']
                    index_number = todos.index(todo_to_edit)
                    todos[index_number] = new_todo.title() + '\n'
                    functions.write_todos(todos)
                    window['todos_key'].update(todos)
                    window['todo_key'].update('')
            except IndexError:
                sg.popup('Select the task to edit.')
        case 'Delete':
            todos = functions.get_todo()
            todo_to_delete = value['todos_key'][0]
            todos.remove(todo_to_delete)
            functions.write_todos(todos)
            window['todos_key'].update(todos)
        case sg.WIN_CLOSED | 'Exit':
            break

window.close()
