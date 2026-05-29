import FreeSimpleGUI as sg
label = sg.Text("Select files to compree")
input1 = sg.Input()
choos_button1 = sg.FileBrowse("Choose", file_types=(("All files", "*.*"),))

label2 = sg.Text("Select files to compree")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose")

compress_button = sg.Button("Compress Files")
layout = [[label, input1, choos_button1], [label2, input2, choose_button2],[compress_button]]
window = sg.Window("File Compression", layout)  
window.read()
window.close()
