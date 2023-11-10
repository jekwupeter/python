import functions
import PySimpleGUI as sg

text = sg.Text("Enter a To-Do")
input_box = sg.InputText(tooltip="enter todo", key="todo")
add_button = sg.Button("Add", key="add")
layout = [[text, input_box, add_button]]
window = sg.Window("To-Do App", layout=layout)

while True:
    event, values = window.read()
    match event:
        case "add":
            functions.Add(values["todo"]+"\n")
            input_box.update("")
        case sg.WIN_CLOSED:
            break
            
window.close()