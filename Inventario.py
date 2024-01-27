import re

with open('archivo2.xml', 'r', encoding='utf-8') as file:
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
    print(f"{matchNum}.- Descripcion del producto: {group}")
    n = matchNum
    for n, match in enumerate(matches2):
        group = match.group(1)
        print(f"  Numero de clave del producto: {group}")
        if matchNum >= n:
            break
    for n, match in enumerate(matches3):
        group = match.group(1)
        print(f"  Cantidad del producto: {group}")
        if matchNum >= n:
            break
    for n, match in enumerate(matches4):
        group = match.group(1)
        print(f"  Valor unitario: {group}\n")
        if matchNum >= n:
            break


#print(xml_data)