"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv

def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla
    contiene  el valor de la segunda columna; la segunda parte de la tupla
    es una lista con las letras (ordenadas y sin repetir letra) de la
    primera  columna que aparecen asociadas a dicho valor de la segunda
    columna.

    Rta/
    [(0, ['C']),
     (1, ['B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E']),
     (4, ['B', 'E']),
     (5, ['B', 'C', 'D', 'E']),
     (6, ['A', 'B', 'C', 'E']),
     (7, ['A', 'C', 'D', 'E']),
     (8, ['A', 'B', 'D', 'E']),
     (9, ['A', 'B', 'C', 'E'])]

    """

    valores = {}
    with open("files/input/data.csv", mode="r", newline="", encoding="utf-8") as datos:
        reader = csv.reader(datos, delimiter='\t')
        for fila in reader:
            letra = fila[0]
            numero = int(fila[1])
            if numero in valores:
                valores[numero].append(letra)
            else:
                valores[numero] = [letra]

    lista_tuplas = []
    for numero in valores:
        letras_no_repetidas = list(set(valores[numero]))
        letras_no_repetidas.sort()
        lista_tuplas.append((numero, letras_no_repetidas))

    lista_tuplas.sort()
    return lista_tuplas

resultado = pregunta_08()
print("El resultado de la lista es: ", resultado)