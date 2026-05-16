"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv

def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """
    lista_tuplas  = [] # tupla

    with open("files/input/data.csv", mode = "r", newline = "", encoding = "utf-8") as datos:
        reader = csv.reader(datos, delimiter = '\t')

        for fila in reader:
            letras = fila[0]
            #print(letras)

            #se lee la columna 4- se separa por comas - ['b','g','f']
            datos = fila[3].split(",")
            contidad_letras_col4 = len(datos)

            #se lee la columna 5 - se separa por comas por grupo de letras "jjj,bbb,ddd,ggg,hhh"
            datos_colum5 = fila[4].split(",")
            contidad_letras_col5 = len(datos_colum5)

            lista_tuplas.append((letras, contidad_letras_col4, contidad_letras_col5))


    return lista_tuplas

resultado = pregunta_10()
print("El resultado de la lista es: ", resultado)
