import csv 
import json
from funciones import calcular_total_ventas

try: 
    with open ("ventas.csv", "r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)

        ventas = []
        for fila in lector:

            venta = {
                'producto' : fila['producto'],
                'precio' : int(fila['precio']),
                'cantidad' : int(fila['cantidad'])
            }

            ventas.append(venta)

            valor_total = calcular_total_ventas(ventas)

            datos = {"Ventas": ventas,"Valor total": valor_total}


except FileNotFoundError:
    print("Error, archivo CSV no encontrado...")


with open("resultado.json","w",encoding="utf-8") as archivo_json:
    json.dump(datos,archivo_json,indent=4,ensure_ascii=False)