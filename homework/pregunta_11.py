"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv

def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
    valores = {}
    with open("files/input/data.csv", mode ="r", newline ="", encoding ="utf-8") as datos:
        reader = csv.reader(datos, delimiter ='\t')

        for fila in reader:
            numero = int(fila[1])           # valor de columna 2
            letras = fila[3].split(",")  # columna 4 - se separa las letras ['b','g','f']
            #print(letras)

            for letra in letras:         # recorre cada letra de la fila
                if letra in valores:
                    valores[letra] = valores[letra] + numero
                else:
                    valores[letra] = numero

    # Se ordena alfabéticamente
    claves_ordenadas = list(valores.keys())
    claves_ordenadas.sort()

    #se reconstruye el diccionario
    diccionario_ordenado = {}
    for clave in claves_ordenadas:
        diccionario_ordenado[clave] = valores[clave]

    return diccionario_ordenado

resultado = pregunta_11()
print("El resultado es: ", resultado)