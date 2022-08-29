## Caminante aleatorio
from Scripts import dibujar_caminantes, dibujar_distancia_promedio

CENTRO = (0,0)
N_CAMINANTES = 5
N_PASOS = 100
N_REPETICIONES = 100
DISTANCIA = 'euclidiana'

def main():    
    dibujar_caminantes(N_CAMINANTES, N_PASOS, CENTRO, DISTANCIA)
    dibujar_distancia_promedio(N_REPETICIONES, N_CAMINANTES, N_PASOS, CENTRO, DISTANCIA)


if __name__ == "__main__":
    main()