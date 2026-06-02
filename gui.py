# Two experiments related to the GUI code.
#
# --- Experiment 1: break vs exit() in the close handler ---
# When the user closes the window, the WIN_CLOSED branch runs:
#
#     case sg.WIN_CLOSED:
#         break
#
# `break` exits the while loop. Anything written AFTER the loop still
# runs:
#
#     while True: ...
#     print("bye")          # runs after break
#     window.close()
#
# If you replace `break` with `exit()` (Python's built-in), the program
# stops IMMEDIATELY — the print and window.close() lines after the
# loop would NOT run.
#
# For a GUI you usually want `break` so any cleanup code after the
# loop (logging, saving state, calling window.close()) still happens.
#
# --- Experiment 2: dynamic layouts ---
# The layout argument doesn't have to be written inline. You can build
# it up first as a regular variable, and pass that variable in.
#
#     button_labels = ["Apply", "Close", "Reset"]
#     layout = []
#     for label_text in button_labels:
#         layout.append([sg.Button(label_text)])
#     window = sg.Window("Demo", layout=layout)
#
# This is essential when the number/contents of buttons or rows depend
# on data you don't know ahead of time (e.g. a list of files from disk).

import FreeSimpleGUI as sg
import functions


label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")

list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=(45, 10))
edit_button = sg.Button("Edit")

window = sg.Window("My To-Do App",
                   layout=[
                       [label],
                       [input_box, add_button],
                       [list_box, edit_button],
                   ],
                   font=("Helvetica", 20))

while True:
    event, values = window.read()
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todos"].update(values=todos)
        case "Edit":
            todo_to_edit = values["todos"][0]
            new_todo = values["todo"]

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo + "\n"
            functions.write_todos(todos)

            window["todos"].update(values=todos)
        case sg.WIN_CLOSED:
            break

print("bye")          # only runs because we use break, not exit()
window.close()
