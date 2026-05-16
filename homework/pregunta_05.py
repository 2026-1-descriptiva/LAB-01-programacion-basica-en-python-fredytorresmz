"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """

    valores = {}
    numero = 0
    with open("files/input/data.csv", mode="r", newline="", encoding="utf-8") as datos:
        reader = csv.reader(datos, delimiter='\t')
        for fila in reader:
            letra = fila[0]
            numero = int(fila[1])
            if letra in valores:
                valores[letra].append(numero)
            else:
                valores[letra] = [numero]

    lista_tuplas = []
    for letra in valores:
        maximo = max(valores[letra])
        minimo = min(valores[letra])
        lista_tuplas.append((letra, maximo, minimo))

    lista_tuplas.sort()
    return lista_tuplas


resultado = pregunta_05()
print("El resultado es: ", resultado)