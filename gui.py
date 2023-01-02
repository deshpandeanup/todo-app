import functions
import PySimpleGUI as sg

label = sg.Text("Type in a Todo")
input_text = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")
window = sg.Window("My Todo App", layout=[[label], [input_text, add_button]])

window.read()
window.close()


