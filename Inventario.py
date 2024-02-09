import re
import os
import pandas as pd
import tkinter as tk
from tkinter import filedialog

carpeta = ''

def seleccionar_carpeta():
    global carpeta
    carpeta = filedialog.askdirectory()
    if carpeta:
        #print(f"Directorio seleccionado: {carpeta}")
        mostrar_archivos(carpeta)
        e1.config(text=f'RUTA: {carpeta}')

def mostrar_archivos(carpeta):
    archivos = os.listdir(carpeta)
    lista_archivos.delete(1.0, tk.END)  # Limpiar el widget de lista
    for archivo in archivos:
        lista_archivos.insert(tk.END, f"{archivo}\n")

def data_xml():
    print("Entrando en ejecucion")
    archivos_xml = [archivo for archivo in os.listdir(carpeta) if archivo.endswith('.xml')]

    lista_descripcion = []
    lista_clave = []
    lista_cantidad = []
    lista_valor = []

    # Iterar sobre la lista de archivos xml
    for archivo_xml in archivos_xml:

        #print('---------- Apertura de archivo ----------')

        with open(os.path.join(carpeta, archivo_xml), 'r', encoding='utf-8') as file:
            xml_data = file.read()

        regex = r'Descripcion="([^"]*)"'
        regex_clave = 'ClaveProdServ="(\d|\w+)"'
        regex_cantidad = 'Cantidad="(\d*.\d*)"'
        regex_valor = 'ValorUnitario="(\d*.\d*)"'

        matches1 = re.finditer(regex, xml_data)
        matches2 = re.finditer(regex_clave, xml_data)
        matches3 = re.finditer(regex_cantidad, xml_data)
        matches4 = re.finditer(regex_valor, xml_data)

        for matchNum, match in enumerate(matches1):
            group = match.group(1)
            #print(f"{matchNum}.- Descripcion del producto: {group}")
            lista_descripcion.append(group)
            n = matchNum
            for n, match in enumerate(matches2):
                group = match.group(1)
                #print(f"  Numero de clave del producto: {group}")
                lista_clave.append(group)
                if matchNum >= n:
                    break
            for n, match in enumerate(matches3):
                group = match.group(1)
                #print(f"  Cantidad del producto: {group}")
                lista_cantidad.append(group)
                if matchNum >= n:
                    break
            for n, match in enumerate(matches4):
                group = match.group(1)
                #print(f"  Valor unitario: {group}\n")
                lista_valor.append(group)
                if matchNum >= n:
                    break
            
        #print('---------- Cierre de archivo ----------')

    data = {'Descripcion': lista_descripcion, 'Clave': lista_clave, 'Cantidad': lista_cantidad, 'Valor unitario': lista_valor}
    data_frame = pd.DataFrame(data)
    data_frame.to_csv(f'{carpeta}/Salida.csv')

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Seleccionador de Directorios")
ventana.geometry('600x400')

# Botón para abrir el seleccionador de directorios
boton_seleccionar = tk.Button(ventana, text="Seleccionar Carpeta", command=seleccionar_carpeta)
boton_seleccionar.pack(pady=20)

e1 = tk.Label(ventana, text='RUTA: Sin ruta')
e1.pack()

lista_archivos = tk.Text(ventana, wrap=tk.WORD, height=10, width=40)
lista_archivos.pack()

btm = tk.Button(ventana, text='Ejecutar', command=data_xml)
btm.pack()

# Iniciar el bucle de eventos
ventana.mainloop()
