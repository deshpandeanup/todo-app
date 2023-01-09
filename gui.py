import functions
import PySimpleGUI as sg
import time
import os


if not os.path.exists("todos.txt"):
    with open(r"C:\Users\anupd\todos.txt", "w") as file:
        pass

sg.theme("GreenMono")


time_label = sg.Text('', key='time_label')
label = sg.Text("Type in a Todo")
input_text = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
edit_button = sg.Button("Edit")
list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=[25, 15])
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window("My Todo App",
                   layout=[[time_label],
                           [label],
                           [input_text, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 10))


while True:

    event, values = window.read(timeout=900)
    window["time_label"].update(value=time.strftime("%b %d %Y %H:%M:%S"))
    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(todos)
        case 'Edit':
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo'] + "\n"
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(todos)
            except IndexError:
                sg.popup("Please select a todo item", font=("Helvetica", 10))
        case 'Complete':
            try:
                todo_to_complete = values["todos"][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select an item first", font=("Tahoma", 10))
        case 'Exit':
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            exit()

window.close()


