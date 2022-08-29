import matplotlib.pyplot as plt
from .Procesos import Caminante

def dibujar_caminantes(n_caminantes:int=1, n_pasos=100, centro=(0,0)):

    fig, ax = plt.subplots(1,1)

    caminantes = { f'caminante_{i}': Caminante(str(i),centro) for i in range(n_caminantes) }
    for caminante in caminantes.values():
        caminante.mover(n_pasos)
        ax.plot(caminante.x, caminante.y, '-o',label=f'caminante_{caminante.nombre}')

    ax.legend()
    plt.show()

    return caminantes




