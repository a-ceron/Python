from email import generator
from numpy import array, exp, log, floor, random

# Funciones de activación
def escalon(y:float, umbral:float=0.)->int:
    """Funcion escalon"""
    return 0 if y < umbral else 1

def lineal(y:float)->float:
    """Funcion lineal"""
    return y

def d_lineal()->int:
    """Derivada de la función lineal"""
    return 1

def sig(y:float)->float:
    """Funcion sigmoide"""
    return 1/(1 + exp(-y))

def d_sig(y:float)->float:
    """Derivada de la funcion sigmoide"""
    return sig(y)*(1 - sig(y))

def softmax(y:array)->array:
    """Funcion softmax"""
    return exp(y)/exp(y).sum()

# Funciones de perdida
# Muchas de estas serán sustituidas por las funciones de sklearn
def ecm(y:array, y_:array)->float:
    """Error cuadratico medio"""
    return 0.5*((y - y_)**2).sum()
    

def dw_ecm(y:array, y_:array, X:array)->array:
    """Derivada de la funcion de perdida ECM"""
    return X.T @ (y_ - y)

def db_ecm(y:array, y_:array)->array:
    """Derivada de la funcion de perdida ECM"""
    return (y_ - y).sum()

def ecb(y:array, y_:array)->float:
    """Entropia cruzada binaria"""
    aux = 0
    for i in range(len(y)):
        aux += y_[i]*log(y[i]) + (1 - y_[i])*log(1 - y[i])
    return -aux

def ecc(y:array, y_:array)->float:
    """Entropia cruzada categorica
    no considera las clases, por lo que se debe hacer para cada clasegit """
    aux = 0
    for i in range(len(y)):
        aux += y_[i]*log(y[i])
    return -aux

def error(y:array, y_:array)->float:
    """Calcula el error"""
    n = y.shape[0]
    return (1/(2*n))*((y - y_)**2).sum()

def dw_error(y:array, y_:array,X:array)->float:
    """Derivada de la funcion de perdida error"""
    n = y.shape[0]
    return (1/(n))*(X.T @ (y - y_) )

def db_error(y:array, y_:array)->float:
    """Derivada de la funcion de perdida error"""
    n = y.shape[0]
    return (1/(n))*(y - y_).sum()

# Otras
def generar_lotes(X:array, y:array, t_lote:int=32)->generator:
    """Genera lotes de tamaño tam_lote"""
    n = X.shape[0]
    n_lotes = int(floor(n/t_lote))

    perm = random.permutation(n)
    X_perm = X[perm]
    y_perm = y[perm]
    for l in range(n_lotes):
        X_lote = X_perm[l*t_lote:(l+1)*t_lote]
        y_lote = y_perm[l*t_lote:(l+1)*t_lote]
        yield l, X_lote, y_lote