# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 16:01:28 2021

@author: Choripan
"""

import PySimpleGUI as sg
import webbrowser
import os
import pdfplumber
import re
import csv

sg.theme('DarkAmber')

lang = 0
length = 0

def job(src_directory, out_directory, lang): 
    global length

    # Getting the files with the format ".pdf" from the requested folder 
    
    list_of_files = []
    
    ext = (".pdf")
    for files in os.listdir(src_directory):
        if files.endswith(ext):
            list_of_files.append(src_directory + "/" + files)
        else:
            continue
    
    length = len(list_of_files)
    
    ticket = []
    date = []
    currency = []
    transaction = []
    quantity = []
    pair = []
    final_price = []
    invested_amount = []
    received_amount = []
    
    # Main loop to scrape the files 
    
    a = 0
    
    for x in list_of_files:
        pdf = pdfplumber.open(list_of_files[0+a])
        page = pdf.pages[0]
        text = page.extract_text()
            
        ticket.append(str(re.findall(r"(?<=COMPROBANTE:\ )([A-Z]{8})", text))) 
        date.append(str(re.findall(r"\d{2}\/\d{2}\/\d{4} \d{2}\:\d{2}", text)))
        currency.append(str(re.findall(r"(?<=Moneda\s)[A-Z]{3,5}", text))) 
        transaction.append(str(re.findall(r"(?<=Operación\s)(Venta [A-Z]{3,5}|Compra [A-Z]{3,5})", text)))
        quantity.append(str(re.findall(r"(?:Cantidad\ {0,10}[A-Z]{3,5})\ {0,10}([0-9]{0,5},[0-9]{0,10})", text))) 
        pair.append(str(re.findall(r"(?:Cotización\ Final\ )([A-Z]{3,5}/[A-Z]{3,5})", text)))
        final_price.append(str(re.findall(r"(?:Cotización\ Final\ )(?:[A-Z]{3,5}/[A-Z]{3,5})\ ([0-9]{1,5},[0-9]{1,10})", text)))
        invested_amount.append(str(re.findall(r"(?:Monto\ invertido\ [A-Z]{3,5}\ )([0-9]{1,5},[0-9]{0,10})", text)))
        received_amount.append(str(re.findall(r"(?:Monto\ recibido\ [A-Z]{3,5}\ )([0-9]{1,5},[0-9]{0,10})", text)))
        pdf.close()
        
        # Formatting the extra [] and '' that were added.
        
        ticket = [re.sub(r'\W', '', i) for i in ticket]     
        date = [re.sub(r'(\[\'|\'\])', '', i) for i in date]
        currency = [re.sub(r'(\[\'|\'\])', '', i) for i in currency]
        transaction = [re.sub(r'(\[\'|\'\])', '', i) for i in transaction]
        quantity = [re.sub(r'(\[\'|\'\])', '', i) for i in quantity]
        pair = [re.sub(r'(\[\'|\'\])', '', i) for i in pair]
        final_price = [re.sub(r'(\[\'|\'\])', '', i) for i in final_price]
        invested_amount = [re.sub(r'(\[\'|\'\])', '', i) for i in invested_amount]
        received_amount = [re.sub(r'(\[\'|\'\])', '', i) for i in received_amount]
        
        if (pdf != None):
            a = a + 1
        else:
            break
        
    # Saving the results to a .csv file
    
    if (lang == 1):
        header = ["Ticket", "Fecha", "Moneda", "Transaccion", "Cantidad", "Par", "Valor final", "Cantidad invertida", "Cantidad recibida"]
    else:
        header = ["Ticket", "Date", "Currency", "Transaction", "Quantity", "Pair", "Final value", "Invested amount", "Received amount"]
    
    with open(out_directory + "/" + "results.csv", "w", encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        
        for w in range(length):
            writer.writerow([ticket[w], date[w], currency[w], transaction[w], quantity[w], pair[w], final_price[w], invested_amount[w], received_amount[w]])


def english():
    global source_directory, output_directory, lang
   
    column0 = [
            
        [sg.FolderBrowse("Source", key = "SR"), sg.InputText(key="SRC")],
        [sg.FolderBrowse("Output", key = "OT"), sg.InputText(key="OTP")],
              ]
    column1 = [
        
        [sg.Button("Help", pad = (25, 5), key = "HP"), sg.Button("Go!", pad = (25,5), key = "GO")],
        
        ]
   
    layout = [
        
              [sg.Frame(layout = column0, title = "")],
              [sg.Frame(layout = column1, title = "", pad = (125,25))],
              [sg.Text("GitHub", pad = (190, 0), text_color = "#FDCB52", enable_events = True, key = "HUB")], ## Update to open the browser on clicking :)
              ]
    window = sg.Window("BuenBit Scrapper", layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "HUB":
            webbrowser.open(r"https://github.com/pacopepe1000?tab=repositories")
        if event == "SR":
            window.Element("SRC").Update("SR")
            source_directory = values["SR"]
        if event == "OT":
            window.Element("OT").Update("OTP")
            output_directory = values["OT"]
        if event == "GO":
            if ((values["SR"] == "") or (values["OT"] == "")): ## Checking to avoid blank input
                sg.popup_error("Something went wrong!")
            else:
                job(values["SR"], values["OT"], lang) ## Passing our arguments to the function job()
                
                if(length == 0): ## Checking if there actually BuenBit tickets in the mentioned directory
                    sg.popup_error("No BuenBit tickets in the source directory!")
                    values["SR"] = "" ## Returning to default, so the user corrects
                    window.Element("SRC").Update("")
                else:
                    sg.popup("File created! in\n" + values["OT"] + "/results.csv")
                    values["SR"] = "" ## Returning to blank so the user can keep using the script
                    values["OT"] = ""
     
        if event == "HP": ## Help! 
            sg.popup("How to use: Click each button to get the folder you want to use, do not type the path in the box. Once finished, click \"Go\"\nSource: Path to where your BuenBit tickets are stored. They have to be in .pdf format.\nOutput: Path where your .csv file will be generated. It will be called \"results.csv\" by default, using UTF-8 encoding.")

def spanish():
    global source_directory, output_directory, lang
    lang = 1
    column0 = [
            
        [sg.FolderBrowse("Fuente", key = "SR"), sg.InputText(key="SRC")],
        [sg.FolderBrowse("Salida", key = "OT"), sg.InputText(key="OTP")],
              ]
    column1 = [
        
        [sg.Button("Ayuda", pad = (25, 5), key = "HP"), sg.Button("Ir!", pad = (25,5), key = "GO")],
        
        ]
   
    layout = [
        
              [sg.Frame(layout = column0, title = "")],
              [sg.Frame(layout = column1, title = "", pad = (125,25))],
              [sg.Text("GitHub", pad = (190, 0), text_color = "#FDCB52", enable_events = True, key = "HUB")], ## Update to open the browser on clicking :)
              ]
    window = sg.Window("BuenBit Scrapper", layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "HUB":
            webbrowser.open(r"https://github.com/pacopepe1000?tab=repositories")
        if event == "SR":
            window.Element("SRC").Update("SR")
            source_directory = values["SR"]
        if event == "OT":
            window.Element("OT").Update("OTP")
            output_directory = values["OT"]
        if event == "GO":
            if ((values["SR"] == "") or (values["OT"] == "")): ## Checking to avoid blank input
                sg.popup_error("Algo salio mal!")
            else:
                job(values["SR"], values["OT"], lang) ## Passing our arguments to the function job()
                
                if(length == 0): ## Checking if there actually BuenBit tickets in the mentioned directory
                    sg.popup_error("No hay tickets de BuenBit en el directorio fuente!")
                    values["SR"] = "" ## Returning to default, so the user corrects
                    window.Element("SRC").Update("")
                else:
                    sg.popup("Archivo creado en\n" + values["OT"] + "/results.csv")
                    values["SR"] = "" ## Returning to blank so the user can keep using the script
                    values["OT"] = ""
     
        if event == "HP": ## Help! 
            sg.popup("Como usar: Clickea en boton para conseguir la carpeta que necesites, no tipees la ruta manualmente. Una vez finalizado, clickea \"Ir\"\nFuente: La ruta donde tus tickets de BuenBit estan guardados. Tienen que estar en formato .pdf.\nSalida: La ruta donde tu archivo .csv va a ser generado. Va a llamarse \"results.csv\" por defecto, usando encodeo UTF-8.")


