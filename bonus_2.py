import FreeSimpleGUI as sg

# Layout
layout = [
    [sg.Text("Enter feet:"), sg.Input()],
    [sg.Text("Enter inches:"), sg.Input()],
    [sg.Button("Cotnvert")]
]

# Create window
window = sg.Window("Convertor", layout)

# Event loop
while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

window.close()