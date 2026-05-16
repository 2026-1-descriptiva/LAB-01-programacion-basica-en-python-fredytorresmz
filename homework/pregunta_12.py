"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv

def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    valores = {}
    with open("files/input/data.csv", mode="r", newline="", encoding="utf-8") as datos:
        reader = csv.reader(datos, delimiter='\t')

        for fila in reader:
            letra = fila[0]                   # columna 1 - letras : 'E', 'A',...
            pares = fila[4].split(",")         # columna 5 - ['jjj:12', 'bbb:3']

            # sumar todos los valores numéricos de la columna 5
            suma_fila = 0
            for par in pares:
                numero = int(par.split(":")[1])   # se extrae el número después de ':'
                suma_fila = suma_fila + numero
                #print(suma_fila)

            # acumular la suma bajo la letra correspondiente
            if letra in valores:
                valores[letra] = valores[letra] + suma_fila
            else:
                valores[letra] = suma_fila

    # Ordenar alfabéticamente igual que pregunta_09 y pregunta_11
    claves_ordenadas = list(valores.keys())
    claves_ordenadas.sort()

    diccionario_ordenado = {}
    for clave in claves_ordenadas:
        diccionario_ordenado[clave] = valores[clave]

    return diccionario_ordenado

resultado = pregunta_12()
print("El resultado es: ", resultado)