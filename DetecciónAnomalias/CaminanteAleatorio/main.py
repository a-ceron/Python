## Caminante aleatorio
from Scripts import dibujar_caminantes, dibujar_distancia_promedio, dibujar_distancias_promedio

CENTRO = (0,0)
N_CAMINANTES = 5
N_PASOS = 100
N_REPETICIONES = 100
DISTANCIA = 'manhattan'

N_ITERACIONES= 10
N_PASOS_MAX = 100

def main():    
    # Un solo número de pasos
    #dibujar_caminantes(N_CAMINANTES, N_PASOS, CENTRO, DISTANCIA)
    #dibujar_distancia_promedio(N_REPETICIONES, N_CAMINANTES, N_PASOS, CENTRO, DISTANCIA)

    # Varios números de pasos
    dibujar_distancias_promedio(N_REPETICIONES, N_CAMINANTES, N_ITERACIONES, N_PASOS_MAX, CENTRO, DISTANCIA)


if __name__ == "__main__":
    main()