"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv

def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """

    sumaColumna = 0
    conteo = {}
    Letras = 0
    with open ("files/input/data.csv", mode = "r", newline = "", encoding = "utf-8") as datos:
        reader = csv.reader(datos, delimiter = '\t')
        for filas in reader:
            Letras = filas[0]
            if Letras in conteo:
                conteo[Letras] = conteo[Letras] + 1
            else:
                conteo[Letras] = 1
            #sumaColumna = sumaColumna + int(filas[1])
            #print(filas)
    #print("La suma es: ", sumaColumna)

    conteo
    lista_tuplas = []
    for letra in conteo:
        lista_tuplas.append((letra, conteo[letra]))

    lista_tuplas.sort()   # Se ordena alfabéticamente por el primer elemento, que es la A
    return lista_tuplas


resultado = pregunta_02()
print("La suma es: ", resultado)