"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv

def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
    valores = {}

    with open("files/input/data.csv", mode="r", newline="", encoding="utf-8") as datos:
        reader = csv.reader(datos, delimiter='\t')
        for fila in reader:
            letras = fila[4].split(",")
            #letras.split(",") #separar por conjunto de letras
            print(letras)
            for numero in letras:
                datos_clave = numero.split(":")[0]
                #valores[numero].append(letras)
                if datos_clave in valores:
                    valores[datos_clave] =  valores[datos_clave] + 1
                else:
                 valores[datos_clave] = 1

    #ordenar por orden alfábetico
    claves_ordenadas = list(valores.keys())
    claves_ordenadas.sort()
    print(claves_ordenadas)

    diccionario_ordenado = {}
    for clave in claves_ordenadas:
        diccionario_ordenado[clave] = valores[clave]


    return diccionario_ordenado

resultado = pregunta_09()
print("El resultado de la lista es: ", resultado)