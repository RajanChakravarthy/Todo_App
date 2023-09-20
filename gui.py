import functions
import PySimpleGUI as sg

label_value = sg.Text('Type in a To-Do')
input_button = sg.InputText(tooltip='Enter todo.')
add_button = sg.Button('Add')

window = sg.Window('To-Do App',layout=[[label_value],
                                            [input_button, add_button]])

window.read()
window.close()
