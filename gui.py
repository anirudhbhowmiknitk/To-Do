import FreeSimpleGUI as sg
import functions

label = sg.Text("Type in a to-do")

input_box = sg.Input(
    key="todo",
    tooltip="Enter a todo"
)

add_button = sg.Button("Add")
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

list_box = sg.Listbox(
    values=functions.get_todos(),
    key="todos",
    enable_events=True,
    size=(45, 10)
)

layout = [
    [label],
    [input_box, add_button],
    [list_box],
    [edit_button, complete_button],
    [exit_button]
]

window = sg.Window(
    "My To-Do App",
    layout=layout,
    font=("Helvetica", 20)
)

while True:
    event, values = window.read()

    if event in (sg.WIN_CLOSED, "Exit"):
        break

    if event == "Add":
        todo = values["todo"].strip()

        if todo:
            todos = functions.get_todos()
            todos.append(todo + "\n")

            functions.write_todos(todos)

            window["todos"].update(values=todos)
            window["todo"].update("")

    elif event == "Edit":

        if not values["todos"]:
            sg.popup("Please select a todo first.")
            continue

        selected_todo = values["todos"][0]
        new_todo = values["todo"].strip()

        todos = functions.get_todos()

        index = todos.index(selected_todo)
        todos[index] = new_todo + "\n"

        functions.write_todos(todos)

        window["todos"].update(values=todos)

    elif event == "Complete":

        if not values["todos"]:
            sg.popup("Please select a todo first.")
            continue

        selected_todo = values["todos"][0]

        todos = functions.get_todos()

        todos.remove(selected_todo)

        functions.write_todos(todos)

        window["todos"].update(values=todos)
        window["todo"].update("")

    elif event == "todos":

        if values["todos"]:
            window["todo"].update(values["todos"][0].strip())

window.close()