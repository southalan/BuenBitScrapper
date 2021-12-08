# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 12:36:49 2021

@author: Choripan
"""

import PySimpleGUI as sg
import interface

# Building the graphical interface 

sg.theme("DarkBrown1")

layout = [[sg.Text("Elige tu lenguaje / Choose your language")], [sg.Button("Español", key = "ES")], [sg.Button("English", key = "EN")]]

## Create the window

window = sg.Window("BuenBit Scrapper", layout)

## Create an event loop

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    
## Choose your language 

    if(event == "ES"):
        window.close()
        interface.spanish()
    if(event == "EN"):
        window.close()
        interface.english()
window.close()



