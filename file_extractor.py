import PySimpleGUI as gui
from file_extractor_func import extract_files


arch_loc_label = gui.Text("Select archive location:")
archive_location = gui.Input()
archive_button = gui.FileBrowse(key="archive_button")

dest_loc_label = gui.Text("Select Destination Directory:")
destination_location = gui.Input()
destination_button = gui.FolderBrowse("Choose", key="destination_button")

extract_button = gui.Button("Extract", key="Extract")
output_message = gui.Text(key="output")

row_1 = gui.Column([[arch_loc_label], [dest_loc_label]])
row_2 = gui.Column([[archive_location], [destination_location]])
row_3 = gui.Column([[archive_button], [destination_button]])

window = gui.Window("Files Extractor", layout=[[row_1, row_2, row_3], [extract_button]])

while True:
    event, values = window.read()
    print(event, values)
    archive_location2 = values["archive_button"]
    destination_location2 = values["destination_button"]
    extract_files(archive_location2, destination_location2)
    window["output"].update(value="Extraction completed successfully")

window.close()


