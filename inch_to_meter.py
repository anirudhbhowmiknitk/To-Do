import PySimpleGUI as sg

label1 = sg.Text("Enter feet:")
input1 = sg.Input(key="feet")

label2 = sg.Text("Enter inches:")
input2 = sg.Input(key="inches")

button = sg.Button("Convert")

output = sg.Text("", key="output")

window = sg.Window(
    "Converter",
    layout=[
        [label1, input1],
        [label2, input2],
        [button, output]
    ]
)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    feet = float(values["feet"])
    inches = float(values["inches"])

    meters = feet * 0.3048 + inches * 0.0254

    window["output"].update(f"{meters:.3f} m")

window.close()