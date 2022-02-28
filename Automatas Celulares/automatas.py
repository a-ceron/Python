import numpy as np

def obtener_estados( regla:int )->list:
    """Dado un número entero regresa su valor en binario de forma inversa
    que se asocian con el estado según la regla dada

    >>> obtener_estados( 30 )
    [0, 1, 1, 1, 1, 0, 0, 0]

    :param regla: Valor entero entre 0 y 255
    :type regla: int
    :return: Lista de estados dados por la regla
    :rtype: list
    """
    return [int(elemento) for elemento in format(regla,'08b')[::-1]]

class celda( object ):
    """Una celda es un objeto que puede ser usado para construir automatas 
    elementales. Se les asocia otras celdas y es más fácil adquirir el valor
    que las domina

    :param valor: Valor inicial de la celda, defaults to 0
    :type valor: int
    """
    def __init__(self, valor:int= 0 ) -> None:
        """Constructor de la clase

        >>> c= celda(0)

        """
        self.valor= valor
        self.previo= None
        self.siguiente= None

    def asignar_valor(self, valor:int)->None:
        """Modificador del valor de la celda

        >>> c.asignar_valor( 1 )

        :param valor: Nuevo valor de la celda
        :type valor: int
        """
        
        self.valor= valor

    def asignar_previo(self, previo:'celda')->None:
        """Asigna a la celda que esta a la izquierda 

        >>> c.asignar_previo( celda(0) )
        
        :param previo: Celda a la izquierda
        :type previo: celda
        """
        self.previo= previo

    def asignar_siguiente(self, siguiente:'celda')->None:
        """Asigna el valor a la derecha de la celda

        >>> c.asignar_previo( celda(0) )

        :param siguiente: Celda a la derecha
        :type siguiente: celda
        """
        self.siguiente= siguiente

    def obtener_estado(self)->int:
        """Regresa el numero en base decimal asociado con 
        el estado que deberá tomar en el siguiente paso
        considerando los estados de la celda y sus vecinos 

        >>> c.obtener_estados()
        4

        :return: Valor del estado siguiente
        :rtype: int
        """
        estado= 0
        if( not ( self.previo is None ) and ( self.previo.valor ) ):
            estado+= 2**2
        if( self.valor ):
            estado+= 2
        if( not ( self.siguiente is None ) and ( self.siguiente.valor ) ):
            estado+= 1

        return estado

    

    
class malla( object ):
    """Contenedor de las celdas. Permite generar figuras asociadas
    a autómatas elementales

    :param filas: Número de celdas iniciales
    :type filas: int
    :param iteraciones: Número de evoluciones
    :type iteraciones: int
    """

    def __init__(self, filas:int, iteraciones:int)->None:
        """Constructor

        >>> m= malla(10,10)

        """
        self.shape= (filas, iteraciones)
        self.generaciones= {}

    def __obtener_primera_generacion( self )-> list:
        """Genera la primera generación, por defecto es un punto en el 
        medio de la longitud inicial de celdas

        :return: Primera generación de celdas
        :rtype: list
        """
        fila= [ celda(0) for _ in range(self.shape[0]) ]
        fila[ int( round( len(fila) / 2 ) ) ].asignar_valor(1)
        self.__asignar_vecinos(fila)
        return fila

    def __asignar_vecinos(self, fila:list)->None:
        """Asigna a los vechinos de cada celda en el espacio

        :param fila: Lista de celdas
        :type fila: list
        """
        for i in range( len(fila) - 1 ):
            fila[i].asignar_siguiente( fila[i + 1] )
            if( i == 0 ):
                continue
            fila[i].asignar_previo( fila[i - 1] )
        fila[len(fila) - 1].asignar_previo(fila[len(fila) - 2])
        

    def obtener_generacion(self, generacion_anterior:list, regla:int )->list:
        """Obtiene la nueva generación de celdas en función de la genración de celdas
        anteriores y la regla de evolución

        >>> m.obtener_generacion( generacion_anterior, regla)

        :param generacion_anterior: Generación anterior de celdas
        :type generacion_anterior: list
        :param regla: Regla de evolución
        :type regla: int
        :return: Nueva lista de celdas
        :rtype: list
        """
        estados= obtener_estados(regla)
        fila= []
        for celd in generacion_anterior:
            fila.append( celda( estados[celd.obtener_estado()] ) )
        self.__asignar_vecinos(fila)
        return fila

    def agregar_generacion(self, nombre:str, generacion:list)->None:
        """Agrega una nueva generación al historico

        >>> m.agregar_generacion( nombre, generacion )

        :param nombre: Nombre de la generación nueva
        :type nombre: str
        :param generacion: Valores de la generación
        :type generacion: list
        """
        self.generaciones[nombre]= generacion

    def evolucionar(self, regla:int=30 )->None:
        """Realiza tantas iteraciones como se hallan asignado según la
        regla dada

        >>> m.evolucionar( )

        :param regla: Regla de evolución, default to 30
        :type regla: int
        """
        generacion_act= self.__obtener_primera_generacion()
        for generacion in range( self.shape[1] ):
            generacion_sig= self.obtener_generacion( generacion_act, regla )
            self.agregar_generacion( f"Generacion {generacion}", generacion_act)
            generacion_act= generacion_sig

    def a_numpy(self)->np.ndarray:
        """Convierte los valores obtenidos en la evolución a una matriz de numpy

        >>> A= m.a_mumpy()
         array([[0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                [0, 0, 0, 1, 1, 0, 0, 1, 0, 0],
                [0, 0, 1, 1, 0, 1, 1, 1, 1, 0],
                [0, 1, 1, 0, 0, 1, 0, 0, 0, 1],
                [1, 1, 0, 1, 1, 1, 1, 0, 1, 1],
                [1, 0, 0, 1, 0, 0, 0, 0, 1, 0],
                [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
                [1, 0, 0, 0, 0, 1, 1, 1, 0, 0],
                [1, 1, 0, 0, 1, 1, 0, 0, 1, 0]])

        :return: Matriz de numpy
        :rtype: np.ndarray
        """
        matrix= []
        for lista in self.generaciones.values():
            fila=[]
            for celda in lista:
                fila.append( celda.valor )
            matrix.append( fila)
        return np.array( matrix )
    
    def graficar(self, titulo:str)->None:
        """Grafica los valores en un mapa de calor
        """

        from matplotlib.pyplot import imshow, show, title
        a= self.a_numpy()
        imshow(a, cmap='hot', interpolation='nearest')
        title(titulo)
        show()


    
