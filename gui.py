import functions
import PySimpleGUI as sg

label_value = sg.Text('Type in a To-Do')
input_button = sg.InputText(tooltip='Enter todo.', key='todo')
add_button = sg.Button('Add')

window = sg.Window('To-Do App',layout=[[label_value],
                                            [input_button, add_button]])

while True:
    event, value = window.read()
    match event:
        case 'Add':
            todo = value['todo']
            todos = functions.get_todo()
            todos.append(todo)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break

window.close()
