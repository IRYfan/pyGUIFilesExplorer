from tkinter import *
from tkinter import ttk
import PySimpleGUI as sg

layout = [[sg.Text('My first one-shot window')],
          [sg.InputText(), sg.InputText()],
          [sg.Submit(), sg.Cancel()],
          ]

window = sg.Window('Window Title', layout)

event, values = window.read()
window.close()

text_input = values[0]
sg.popup('You entered', text_input)

# Use PySimpleGUI to create a similar programm like the first java program
# progress bar?
