"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv

def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    valores = {}
    with open("files/input/data.csv", mode="r", newline="", encoding="utf-8") as datos:
        reader = csv.reader(datos, delimiter='\t')
        for fila in reader:
            # se parte cada sección y se separa por comas -- ['jjj:12', 'bbb:3', 'ddd:9']
            pares = fila[4].split(',')
            for par in pares:
                # 'jjj:12' → clave='jjj', numero=12
                clave = par.split(':')[0] # posición
                numero = int(par.split(':')[1])
                if clave in valores:
                    valores[clave].append(numero)
                else:
                    valores[clave] = [numero]

    lista_tuplas = []
    for clave in valores:
        minimo = min(valores[clave])
        maximo = max(valores[clave])
        lista_tuplas.append((clave, minimo, maximo))

    lista_tuplas.sort()
    
    return lista_tuplas

resultado = pregunta_06()
print("El resultado organizado es: ", resultado)