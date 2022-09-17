from numpy import array, zeros, random, floor
from .herramientas import ecm, dw_ecm, db_ecm, generar_lotes
from sklearn.metrics import mean_squared_error as mse

def neurona(X:array, W:array, b:array)->float:
    return X @ W + b 

# Regresión lineal mediante descenso por gradiente
def desenso_gradiente(X, y, n_epocas:int=10, tasa:float=0.001, err=None):
    """Vamos a entrenar un modelo de regresión lineal usando descenso por gradiente. En particular, buscaremos minimizar la pérdida de suma de errores cuadráticos."""
    if err is None:
        f_err = ecm
        dw_err = dw_ecm
        db_err = db_ecm
    else:
        f_err = err[0]
        dw_err = err[1]
        db_err = err[2]

    hist = zeros(n_epocas)

    # Inicializamos los pesos y el sesgo
    W = random.rand(X.shape[1], 1, ) # Es una matriz de tamaño (X.shape[1], 1)
    b = zeros((1, 1)) # Es un escalar [[0]]

    # Descenso por gradiente
    for e in range(n_epocas):   #Note que usamos e (error) como variable de iteración
        y_ = neurona(X, W, b)   #Calculamos la salida de la neurona
        hist[e] = f_err(y,y_) #mse(y, y_)    #Calculamos el error
        W -= tasa * dw_err(y, y_, X)    #Actualizamos los pesos
        b -= tasa * db_err(y, y_)       #Actualizamos el sesgo

    return W, b, hist

def descenso_gradiente_estocastico(X, y, n_epocas:int=10, t_lote:int=10, tasa:float=0.01, err=None):
    if err is None:
        f_err = ecm
        dw_err = dw_ecm
        db_err = db_ecm
    else:
        f_err = err[0]
        dw_err = err[1]
        db_err = err[2]
        
    hist = zeros(n_epocas)
    hist_lotes = zeros((n_epocas, int(floor(X.shape[0]/t_lote))))

    # Inicializamos los pesos y el sesgo
    W = random.rand(X.shape[1], 1, ) # Es una matriz de tamaño (X.shape[1], 1)
    b = zeros((1, 1)) # Es un escalar [[0]]

    # Descenso por gradiente
    for e in range(n_epocas):   #Note que usamos e (error) como variable de iteración
        y_ = neurona(X, W, b)
        hist[e] = f_err(y, y_)
        for l, Xlote, ylote in generar_lotes(X,y,t_lote):
            y_ = neurona(Xlote, W, b)
            hist_lotes[e, l] = f_err(ylote, y_)
            W -= tasa * dw_err(ylote, y_, Xlote)
            b -= tasa * db_err(ylote, y_)

    return W, b, hist, hist_lotes

