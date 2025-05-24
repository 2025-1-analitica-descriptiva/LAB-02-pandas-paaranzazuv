"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
import pandas as pd

def pregunta_06():
    df = pd.read_csv("files/input/tbl1.tsv", sep="\t")
    respuesta = df['c4'].unique().tolist()
    lista=[]
    for i in range(len(respuesta)):
        respuesta[i] = respuesta[i].upper()
        lista.append(respuesta[i])
    lista.sort()
    return lista


"""
    Retorne una lista con los valores unicos de la columna `c4` del archivo
    `tbl1.csv` en mayusculas y ordenados alfabéticamente.

    Rta/
    ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    """
