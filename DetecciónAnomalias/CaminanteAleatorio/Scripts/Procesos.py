import random

class Caminante():
    """Caminante aleatorio

    :param x: _description_, defaults to 0
    :type x: int, optional
    :param y: _description_, defaults to 0
    :type y: int, optional
    """

    def __init__(self, nombre:str, centro=(0,0)):
        """Constructor
        """
        self.x = centro[0]
        self.y = centro[1]
        self.centro = centro
        self.nombre = nombre

    def mover(self, pasos:int, prob:list=[0.25, 0.25, 0.25, 0.25])->list:
        direcciones = [0,1,2,3] #Difrerentes tipos de mocimiento, arriba, abajo, izquierda, derecha
        movimientos= random.choices(direcciones, prob, k=pasos) #Se elige una lista de movimientos aleatorios
        
        camino = []
        for movimiento in movimientos:
            camino.append((self.x, self.y))
            self.mueve(movimiento, 1)
            
        return camino

    def mueve(self, direccion:int, distancia:int):
        if direccion == 0:
            self.y += distancia
        elif direccion == 1:
            self.y -= distancia
        elif direccion == 2:
            self.x -= distancia
        elif direccion == 3:
            self.x += distancia
            
    def distancia(self, centro:tuple=None, tipo="euclidiana"):
        distancia= getattr(metrica, tipo)
        return distancia((self.x,self.y), centro) if centro is not None else distancia((self.x,self.y), self.centro)

class metrica():

    def euclidiana(X,Y)->float:
        """Calcula la distancia ecuclidiana entre dos puntos

        :param X: Punto 1
        :type X: tuple
        :param Y: Punto 2
        :type Y: tuple
        :return: Distancia entre los dos puntos
        :rtype: float
        """
        return ((X[0]-Y[0])**2 + (X[1]-Y[1])**2)**(1/2)

    def manhattan(X,Y)->float:
        """Calcula la distancia Manhattan entre dos puntos

        :param X: Punto 1
        :type X: tuple
        :param Y: Punto 2
        :type Y: tuple
        :return: Distancia entre los dos puntos
        :rtype: float
        """
        return abs(X[0]-Y[0]) + abs(X[1]-Y[1])

    def chebyshev(X,Y)->float:
        """Calcula la distancia Chebyshev entre dos puntos

        :param X: Punto 1
        :type X: tuple
        :param Y: Punto 2
        :type Y: tuple
        :return: Distancia entre los dos puntos
        :rtype: float
        """
        return max(abs(X[0]-Y[0]), abs(X[1]-Y[1]))

    def minkowski(X,Y, p:int=2)->float:
        """Calcula la distancia Minkowski entre dos puntos

        :param X: Punto 1
        :type X: tuple
        :param Y: Punto 2
        :type Y: tuple
        :param p: Exponente, defaults to 2
        :type p: int, optional
        :return: Distancia entre los dos puntos
        :rtype: float
        """
        return ((abs(X[0]-Y[0])**p + abs(X[1]-Y[1])**p)**(1/p))

    