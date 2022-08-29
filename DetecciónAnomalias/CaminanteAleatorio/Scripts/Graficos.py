from cProfile import label
import matplotlib.pyplot as plt
from .Procesos import Caminante

def calcular_caminos(centro, n_caminantes, n_pasos, simplificado:bool=True):
    caminantes = { f'caminante_{i}': [Caminante(str(i),centro)] for i in range(n_caminantes) }
    for caminante in caminantes:
        caminantes[caminante].append(caminantes[caminante][0].mover(n_pasos))

    return caminantes if not simplificado else { caminante: caminantes[caminante][0] for caminante in caminantes } 

def dibujar_caminantes(n_caminantes:int=1, n_pasos=100, centro=(0,0), plot:bool=True):

    _, ax = plt.subplots(1,1)

    caminantes = calcular_caminos(centro, n_caminantes, n_pasos)
    
    if plot:
        for caminante in caminantes:
            x = [caminante[0] for caminante in caminantes[caminante][1]]
            y = [caminante[1] for caminante in caminantes[caminante][1]]
            ax.plot(x, y, 'o-',label=f'caminante_{caminantes[caminante][0].nombre}')

        ax.plot(centro[0], centro[1], "o", color="black", label='Centro')

        ax.legend()
        ax.grid()
        plt.show()

def dibujar_distancia_promedio(n_repeticiones:int, n_caminantes, n_pasos, centro):
    distancias = []
    distancias_promedio = []
    for _ in range(n_repeticiones):
        caminantes = calcular_caminos(centro, n_caminantes, n_pasos, simplificado=True)
        distancias.append(sum([caminante.distancia() for caminante in caminantes.values()])/len(caminantes))
        distancias_promedio.append(sum(distancias)/len(distancias))


    plt.plot(distancias)
    plt.show()



