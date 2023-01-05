import PySimpleGUI as sg
from zip_creator import make_archive

label1 = sg.Text("Select Files to compress")
input1 = sg.Input()
choose_button1 = sg.FilesBrowse("Choose", key="filepaths")

label2 = sg.Text("Select Destination")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key="dest_dir")

compress_button = sg.Button("Compress")

message = sg.Text(key="output", text_color="Orange")

window = sg.Window("File Compression Tool", layout=[[label1, input1, choose_button1],
                                                    [label2, input2, choose_button2],
                                                    [compress_button, message]])

while True:
    event, values = window.read()
    print(f'event: + {event}')
    print(f'values: + {values}')
    filepaths = values["filepaths"].split(";")
    folder_path = values["dest_dir"]
    make_archive(filepaths, folder_path)
    print(filepaths)
    print(folder_path)
    window["output"].update(value="Compression completed..")

window.read()
window.close()
