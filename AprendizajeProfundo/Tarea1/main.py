from cProfile import label
from sklearn.model_selection import train_test_split 
from dotenv import load_dotenv
from pandas import read_csv
from os import getenv
from numpy import newaxis, arange
from numpy import random
import matplotlib.pyplot as plt

from scripts import desenso_gradiente, descenso_gradiente_estocastico, error, dw_error, db_error

N_EPOCAS = 10
TASA = 0.001
SEMILLA = 42
LOTE = 32

def init():
    # Cargamos los datos
    load_dotenv()
    random.seed(SEMILLA)
    sat = read_csv(getenv("URL_DATOS_SAT"), sep=' ')

    X = sat.comp_GPA.to_numpy()[:, newaxis]
    y= sat.univ_GPA.to_numpy()[:, newaxis]

    # Dividimos el conjunto de datos en entrenamiento y prueba
    X_ent, X_val, y_ent, y_val = train_test_split(X, y, test_size=0.2, random_state=42)
    X_rango = arange(2.0, 4.0, 0.01)[:, newaxis].T # Vector de valores de 2 a 4 con aumento 0.01

    return X_ent, X_val, y_ent, y_val, X_rango

def graficar_error_cuadrado(hist):
    plt.plot(hist)
    plt.xlabel("Época")
    plt.ylabel("Error cuadrático medio")
    plt.show()

def graficar_curva_ajustada(X_ent, y_ent, X_rango, W, b):
    y_rango_dg = X_rango.T @ W + b

    plt.scatter(X_ent[:, 0], y_ent[:, 0], label='Datos de entrenamiento')
    plt.plot(X_rango.T[:, 0], y_rango_dg[:, 0], 'r', label='Ajuste')
    plt.xlabel("$X$")
    plt.ylabel("$y$")
    plt.legend()
    plt.show()


def regresion_lineal():
    def desenso_lineal(X_ent, y_ent, X_rango):
        wdg, bdg, histdg = desenso_gradiente(X_ent, 
                                            y_ent,
                                            n_epocas=N_EPOCAS, 
                                            tasa=TASA)
        graficar_error_cuadrado(histdg)
        graficar_curva_ajustada(X_ent, y_ent, X_rango, wdg, bdg)

    def desenso_estocatico(X_ent, y_ent, X_rango):
        wdes, bdes, histdes, histdes_lote = descenso_gradiente_estocastico(X_ent,
                                                                        y_ent,
                                                                        n_epocas=N_EPOCAS,
                                                                        tasa=TASA,
                                                                        t_lote=LOTE)

        graficar_error_cuadrado(histdes)
        graficar_curva_ajustada(X_ent, y_ent, X_rango, wdes, bdes)

    X_ent, X_val, y_ent, y_val, X_rango = init()
    desenso_lineal(X_ent, y_ent, X_rango)
    desenso_estocatico(X_ent, y_ent, X_rango)

def regresion_lineal_ejercicio():
    def desenso_lineal(X_ent, y_ent, X_rango):
        wdg, bdg, histdg = desenso_gradiente(X_ent, 
                                            y_ent,
                                            n_epocas=N_EPOCAS, 
                                            tasa=TASA,
                                            err=[error, dw_error, db_error])
        graficar_error_cuadrado(histdg)
        graficar_curva_ajustada(X_ent, y_ent, X_rango, wdg, bdg)

    def desenso_estocatico(X_ent, y_ent, X_rango):
        wdes, bdes, histdes, histdes_lote = descenso_gradiente_estocastico(X_ent,
                                                                        y_ent,
                                                                        n_epocas=N_EPOCAS,
                                                                        tasa=TASA,
                                                                        t_lote=LOTE,err=[error, dw_error, db_error])

        graficar_error_cuadrado(histdes)
        graficar_curva_ajustada(X_ent, y_ent, X_rango, wdes, bdes)
        
    X_ent, X_val, y_ent, y_val, X_rango = init()
    desenso_lineal(X_ent, y_ent, X_rango)
    desenso_estocatico(X_ent, y_ent, X_rango)


def main():
    regresion_lineal_ejercicio()
    

if __name__ == "__main__":
    main()
