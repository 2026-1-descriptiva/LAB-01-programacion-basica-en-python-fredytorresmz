"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv

def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]

    """

    conteo = {}
    with open("files/input/data.csv", mode="r", newline="", encoding="utf-8") as datos:
        reader = csv.reader(datos, delimiter ='\t')
        for fila in reader:
            mes = fila[2].split('-')[1]   # se busca ayuda de la función split y separar por guión:  "1999-02-28" = "02"
            if mes in conteo:
                conteo[mes] = conteo[mes] + 1
            else:
                conteo[mes] = 1

    lista_tuplas = []
    for mes in conteo:
        lista_tuplas.append((mes, conteo[mes]))

    lista_tuplas.sort() # lista ordenada
    return lista_tuplas

resultado = pregunta_04()
print("El resultado es: ", resultado)