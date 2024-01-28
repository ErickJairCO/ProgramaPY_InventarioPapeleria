import re
import os
import pandas as pd

carpeta = 'D:/Erick/PROYECTOS/PoryectosVisualPython/InventarioPapeleria'
archivos_xml = [archivo for archivo in os.listdir(carpeta) if archivo.endswith('.xml')]

lista_descripcion = []
lista_clave = []
lista_cantidad = []
lista_valor = []

# Iterar sobre la lista de archivos xml
for archivo_xml in archivos_xml:

    #print('---------- Apertura de archivo ----------')

    with open(archivo_xml, 'r', encoding='utf-8') as file:
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

data = {'Descripcion':lista_descripcion, 'Clave':lista_clave, 'Cantidad':lista_cantidad, 'Valor unitario':lista_valor}
data_frame = pd.DataFrame(data)
data_frame.to_csv('Salida.csv')

    #print(xml_data)