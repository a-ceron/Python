from pandas import read_csv, DataFrame
from numpy import random, where, array

def leer_datos(path:str)->DataFrame:
    """regresa el DataFrame de un archivo"""
    return read_csv(path)

def obtener_valores(n:int=10000, path:str=None)->list:
    """Regresa una lista de valores aleatorios distribuidos normalmente 
    con los parámetros del archivo"""

    df = leer_datos(path)

    media = df.total.mean() #Vector de personas con el rango de edad
    desviacion = df.total.std()

    #todo: mejorar esto
    normal= normalizar(random.normal(media, desviacion, df.shape[0] - 1))
    while sum(where(normal < 0, 1, 0)) > 0:
        normal= normalizar(random.normal(media, desviacion, df.shape[0] - 1))
    return obtener_edades( [round(n*x) for x in normal] )

def obtener_edades(num_edades:list)->list:
    edades = []
    for i in range(len(num_edades)):
        edades.extend(random.uniform(i*5, (i + 1)*5, num_edades[i]))
    
    return array([round(edad) for edad in edades])

def normalizar(datos):
    total = sum(datos)
    return array([dato/total for dato in datos])