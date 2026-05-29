import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
inputbock = sg.InputText(tooltip="Type in a to-do")
addbutton = sg.Button("Add")
window = sg.Window("My To-Do App", layout=[[label,inputbock, addbutton]])
window.read()
window.close()
