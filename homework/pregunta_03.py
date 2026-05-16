"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv

def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """

   
    conteo = {}
    Letras = 0
    with open ("files/input/data.csv", mode = "r", newline = "", encoding = "utf-8") as datos:
        reader = csv.reader(datos, delimiter = '\t')
        for filas in reader:
            Letras = filas[0]
            valor = int(filas[1])
            if Letras in conteo:
                conteo[Letras] = conteo[Letras] + valor
            else:
                conteo[Letras] = valor
            #sumaColumna = sumaColumna + int(filas[1])
            #print(filas)
    #print("La suma es: ", sumaColumna)

    lista_tuplas = []
    for letra in conteo:
        lista_tuplas.append((letra, conteo[letra]))

    lista_tuplas.sort()   # Se ordena alfabéticamente por el primer elemento, que es la A
    return lista_tuplas


resultado = pregunta_03()
print("El resultado es: ", resultado)
