# def speed(distance, time):
#     return distance / time
#
#
# print(speed(200, 4))
#
#
# def speed(distance, time):
#     return distance / time
#
#
# print(speed(time=5, distance=300))


# def calculate_time(h, g=9.80665):
#     t = (2 * h / g) ** 0.5
#     return t
#
#
#
# time = calculate_time(100)
# print(time)

import PySimpleGUI as sg


def km_to_miles(km):
    return float(km * 1.6)


label = sg.Text("Kilometers: ")
input_box = sg.InputText(tooltip="Enter todo", key="kms")
miles_button = sg.Button("Convert")

output = sg.Text(key="output")

window = sg.Window('Km to Miles Converter',
                   layout=[[label, input_box], [miles_button, output]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read()
    match event:
        case "Convert":
            km = float(values["kms"])
            result = km_to_miles(km)
            window['output'].update(value=result)
        case sg.WIN_CLOSED:
            break

window.close()