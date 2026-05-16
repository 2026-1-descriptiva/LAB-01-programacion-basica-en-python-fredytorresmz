"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv
"""
sumaColumna = 0
with open ("files/input/data.csv", mode = "r", newline = "", encoding = "utf-8") as datos:
    reader = csv.reader(datos, delimiter='\t')
    for filas in reader:
        sumaColumna = sumaColumna + int(filas[1])
print("La suma es: ", sumaColumna)
"""

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    sumaColumna = 0
    with open ("files/input/data.csv", mode = "r", newline = "", encoding = "utf-8") as datos:
        reader = csv.reader(datos, delimiter='\t')
        for filas in reader:
            sumaColumna = sumaColumna + int(filas[1])
            #print(filas)
    #print("La suma es: ", sumaColumna)
    return sumaColumna

resultado = pregunta_01()
print("La suma es: ", resultado)