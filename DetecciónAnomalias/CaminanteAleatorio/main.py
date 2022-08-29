## Caminante aleatorio
from Scripts import dibujar_caminantes

def main():    
    caminantes = dibujar_caminantes(5,10)
    distancia_promedio= sum([caminante.distancia() for caminante in caminantes.values()])/len(caminantes)
    print(f"Distancia promedio: {distancia_promedio}")

    n_repeticiones= 100

if __name__ == "__main__":
    main()