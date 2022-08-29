from math import ceil
import matplotlib.pyplot as plt
from .Procesos import Caminante

def calcular_caminos(centro:tuple, n_caminantes:int, n_pasos:int, simplificado:bool=False):
    """Calcula los caminos de los caminantes y los devuelve en un diccionario

    :param centro: Centro de los caminantes, desde donde comienzan a caminar
    :type centro: tupple
    :param n_caminantes: Número de caminantes
    :type n_caminantes: int
    :param n_pasos: Número de pasos a dar por los caminantes
    :type n_pasos: int
    :param simplificado: Define el tipo de diccionario a regresar, defaults to False
    :type simplificado: bool, optional
    :return: Caminantes después de moverse n_pasos
    :rtype: dict
    """
    caminantes = { f'caminante_{i}': [Caminante(str(i),centro)] for i in range(n_caminantes) }
    for caminante in caminantes:
        caminantes[caminante].append(caminantes[caminante][0].mover(n_pasos))

    return caminantes if not simplificado else { caminante: caminantes[caminante][0] for caminante in caminantes } 

def dibujar_caminantes(n_caminantes:int=1, n_pasos:int=100, centro:tuple=(0,0),tipo:str="euclidiana"):
    """Dibuja el camino de los caminantes

    :param n_caminantes: Número de caminantes, defaults to 1
    :type n_caminantes: int, optional
    :param n_pasos: Número de pasos, defaults to 100
    :type n_pasos: int, optional
    :param centro: Punto de origen de los caminantes, defaults to (0,0)
    :type centro: tuple, optional
    :param tipo: Tipo de métrica a utilizar, defaults to "euclidiana"
    :type tipo: str, optional
    """

    _, ax = plt.subplots(1,1)

    caminantes = calcular_caminos(centro, n_caminantes, n_pasos)
    
    for caminante in caminantes:
        x = [caminante[0] for caminante in caminantes[caminante][1]]
        y = [caminante[1] for caminante in caminantes[caminante][1]]
        ax.plot(x, y, 'o-',label=f'caminante_{caminantes[caminante][0].nombre}')

    ax.plot(centro[0], centro[1], "o", color="black", label='Centro')
    ax.legend()
    ax.grid()

    plt.show()

    distancia_promedio= sum([caminante[0].distancia(tipo=tipo) for caminante in caminantes.values()])/len(caminantes)
    print(f"Distancia promedio: {distancia_promedio}")

def dibujar_distancia_promedio(n_repeticiones:int, n_caminantes:int, n_pasos:int, centro:tuple, tipo:str):
    """Grafica la distancia pormedio después de n_repeticiones

    :param n_repeticiones: Número de veces que se repite el experimento
    :type n_repeticiones: int
    :param n_caminantes: Número de caminantes por experimento
    :type n_caminantes: int
    :param n_pasos: N´umero de pasos
    :type n_pasos: int
    :param centro: Punto de origen de los caminantes
    :type centro: tuple
    :param tipo: Tipo de métrica a utilizar
    :type tipo: str
    """  
    distancias = []
    distancias_promedio = []
    for _ in range(n_repeticiones):
        # Obtengo el diccionario de caminantes después de haber realizado n_pasos
        caminantes = calcular_caminos(centro, n_caminantes, n_pasos, simplificado=True)

        # Calculo la distancia promedio de los caminantes después de haber realizado n_pasos
        distancias.append(sum([caminante.distancia(tipo=tipo) for caminante in caminantes.values()])/len(caminantes))
        distancias_promedio.append(sum(distancias)/len(distancias)) ## Distancia promedio de las distancias


    plt.plot(distancias, label='Distancias en cada epoca')
    plt.plot(distancias_promedio, label='Distancia promedio')

    plt.legend()
    plt.grid()
    plt.show()

def dibujar_distancias_promedio(n_repeticiones:int, n_caminantes:int, n_iteraciones:int, n_pasos_max:int, centro:tuple, tipo:str):
    """Grafica la distancia promedio en cada iteración

    :param n_repeticiones: Número de veces que se repite el experimento
    :type n_repeticiones: int
    :param n_caminantes: Número de caminantes por experimento
    :type n_caminantes: int
    :param n_iteraciones: Número de iteraciones
    :type n_iteraciones: int
    :param n_pasos_max: Número máximo de pasos
    :type n_pasos_max: int
    :param centro: Punto de origen de los caminantes
    :type centro: tuple
    :param tipo: Tipo de métrica a utilizar
    :type tipo: str
    """  
    distancias_promedio = []
    for i in range(1,n_pasos_max,int(ceil(n_iteraciones/n_pasos_max))):
        distancias = []
        for _ in range(n_repeticiones):
            # Obtengo el diccionario de caminantes después de haber realizado n_pasos
            caminantes = calcular_caminos(centro, n_caminantes, i+1, simplificado=True)

            # Calculo la distancia promedio de los caminantes después de haber realizado n_pasos
            distancias.append(sum([caminante.distancia(tipo=tipo) for caminante in caminantes.values()])/len(caminantes))
        distancias_promedio.append(sum(distancias)/len(distancias)) ## Distancia promedio de las distancias

    plt.plot(distancias_promedio, label='Distancia promedio')
    plt.bar(range(len(distancias_promedio)), distancias_promedio, label='Distancia promedio')

    print(f"Distancia promedio: {distancias_promedio[-1]}")
    print(f"Maxima distancia: {max(distancias_promedio)}")
    print(f"Minima distancia: {min(distancias_promedio)}")

    plt.legend()
    plt.grid()
    plt.show()



