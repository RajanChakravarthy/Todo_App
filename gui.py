import functions
import PySimpleGUI as sg

label_value = sg.Text('Type in a To-Do')
input_button = sg.InputText(tooltip='Enter todo.', key='todo_key')
add_button = sg.Button('Add')

list_button = sg.Listbox(functions.get_todo(),size=(50,10), key='todos_key',enable_events=True)
edit_button = sg.Button('Edit')

window = sg.Window('To-Do App',
                   layout=[[label_value],
                        [input_button, add_button],
                        [list_button, edit_button]],
                   font= ('Arial Bold',12))

while True:
    event, value = window.read()
    print(event)
    print(value)
    match event:
        case 'Add':
            todo = value['todo_key'] + '\n'
            todos = functions.get_todo()
            todos.append(todo)
            functions.write_todos(todos)
            window['todos_key'].update(todos)
        case 'Edit':
            todos = functions.get_todo()
            todo_to_edit = value['todos_key'][0]
            new_todo = value['todo_key']
            index_number = todos.index(todo_to_edit)
            todos[index_number] = new_todo + '\n'
            functions.write_todos(todos)
            window['todos_key'].update(todos)

        case sg.WIN_CLOSED:
            break

window.close()
