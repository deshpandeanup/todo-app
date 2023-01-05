import PySimpleGUI as sg
import convert


enter_feet_label = sg.Text("Enter Feet")
feet_input_box = sg.InputText(key="feet",tooltip="Enter Feet")

enter_inches_label = sg.Text("Enter Inches")
inches_input_box = sg.InputText(key="inches", tooltip="Enter Inches")

convert_button = sg.Button("Convert")
output_message = sg.Text(key="Output", text_color="orange")

window = sg.Window("Convertor", layout=[[enter_feet_label, feet_input_box],
                                       [enter_inches_label, inches_input_box],
                                       [convert_button, output_message]])

while True:
    event, values = window.read()
    feet_value = values["feet"]
    inch_value = values["inches"]
    conversion_value = convert.convert_into_metres(feet_value, inch_value)

    window["Output"].update(value=f"{conversion_value} m")


window.close()