from math import sqrt
import scipy.spatial.distance as measure


class punto( object ):  
    """Genera coordenadas en un espacio dos dimensional

    :param x: Coordenada en el eje de las absisas
    :type x: float
    :param y: Coordenada en el eje de las ordenadas
    :type y: float
    """  
    def __init__( self, x:float, y:float )->None: 
        """Constructor
        """
        self.x= x
        self.y= y
        
    def obtener_x(self)->float:
        """Regresa el valor de la coordenada en abscisas

        :return: Coordenada en el eje de las absisas
        :rtype: float
        """

        return self.x
    
    def obtener_y(self)->float:
        """Regresa el valor de la coordenada ordenada

        :return: Valor de la coordenada
        :rtype: float
        """
        return self.y
    
    def obtener_coord(self)->tuple:
        """Regresa el par de coordenadas como tupla

        :return: Coordenadas del punto
        :rtype: tuple
        """
        return( self.obtener_x(), self.obtener_y() )
    
    def fijar_x(self,x:float)->None:
        """Reasigna el valor de la coordenada en las abscisas

        :param x: Nuevo valor de la coordenada
        :type x: float
        """
        self.x= x
    
    def fijar_y(self,y:float)->None:
        """Reasigna el valor de la coordenada en las ordenadas

        :param y: Nuevo valor de la coordenada
        :type y: float
        """
        self.y= y

class segmento( object ):
    """Genera una porción de línea recta comprendida entre dos puntos extremos P1, P2

    :param P1: Extremo inicial
    :type P1: punto
    :param P2: Extremo final
    :type P2: punto
    """
    def __init__(self, A:punto, B:punto ):
        """Constructor
        """
        self.P1= A
        self.P2= B
        self.longitud= medidas.euclidiana(self.P1, self.P2)
    
    def obtener_punto_razon(self,r:float)->tuple:
        """Si P1, P2 son los extremos de un segmento P1P2, el punto Q que divide a este segmento en la razón dada
        r= P1Q : P2Q son
            x= \frac{x_1 + rx_2}{1 + r}; y= \frac{y_1 + ry_2}{1 + r}, r\neq -1

        :param r: Razón dada
        :type r: float
        :return: Coordenadas del punto Q
        :rtype: tuple
        """
        if( r == -1 ):
            raise ValueError(f"r no puede tomar el valor {r}")
        x= (self.P1.obtener_x() + r * self.P2.obtener_x()) / ( 1 + r)
        y= (self.P1.obtener_y() + r * self.P2.obtener_y()) / ( 1 + r)

        return( x, y)

    def obtener_punto_medio(self)->tuple:
        """Caso cuando la razón es la unidad

        :return: Punto medio del segmento
        :rtype: tuple
        """
        return self.obtener_punto_razon(1)

    def obtener_punto_ini(self)->punto:
        """Regresa el extremo inicial del segmento

        :return: Extremo inicial
        :rtype: punto
        """
        return self.P1
    
    def obtener_punto_fin(self)->punto:
        """Regresa el extremo final del segmento

        :return: Extremo final
        :rtype: punto
        """
        return self.P2
    
class triangulo( object ):
    """Intento generar un objeto triángulo que adquiere las 
    propiedades de un triángulo conocido

    :param a: Vetice del triángulo 
    :type a: punto
    :param b: Vértice del triángulo 
    :type b: punto
    :param c: Vértice del triángulo 
    :type c: punto
    """
    def __init__(self, a:punto, b:punto, c:punto)->None:
        """Constructor
        """
        self.A= a
        self.B= b
        self.C= c
        
    def obtener_aristas(self)->tuple:
        """Regresa tres segmentos de recta relacionados con los lados del triángulo como 
        objetos del tipo segmento

        :return: Triada de segmentos
        :rtype: tuple
        """
        return segmento( self.A, self.B ), segmento( self.A, self.C ), segmento( self.C, self.B )
        
    def obtener_vertices(self)->tuple:
        """Regresa los vértices del triángulo como objetos de tipo coordenadas

        :return: Vertices
        :rtype: tuple
        """
        return self.A, self.B, self.C

    def obtener_area(self)->float:
        """Área usando la fórmula de heron

        :return: Área del triángulo
        :rtype: float
        """
        a,b,c= self.obtener_aristas()
        s= ( a.longitud() + b.longitud() + c.longitud() ) / 2

        return sqrt( s*( s - a.longitud() )*( s - b.longitud() )*( s - c.longitud() ) )
    
    def obtener_perimetro(self)->float:
        """Regresa el perímetro del triángulo

        :return: Perimetro
        :rtype: float
        """
        a, b, c= self.obtener_aristas()
        return a.longitud() + b.longitud() + c.longitud()

class medidas( object ):
    """Diferentes medidas entre puntos
    """
    def euclidiana(self, P1:punto, P2:punto)->float:
        """En un sistema coordenado lineal, la longitud del segmento dirigido
        que une dos puntos dados se obtiene, en magnitud y signo, restando la coordenada de origen 
        de la coordenada del extremo. La distancia entre dos puntos dados P1, P2 esta dada por la fórmula
            d= \sqrt{ (x_1 - x_2)^2 + (y_1 - y_2)^2 }

        :param P1: Punto inicial
        :type P1: punto
        :param P2: Punto final
        :type P2: punto
        :return: Longitud del segmento dirigido
        :rtype: float
        """
        return measure.euclidean( P1.obtener_coord(), 
                          P2.obtener_coord() )

    def manhattan(self, P1:punto, P2:punto)->float:
        """Regresa la distancia manhattan entre dos puntos

        :param P1: Punto inicial
        :type P1: punto
        :param P2: Punto final
        :type P2: punto
        :return: Longitud del segmento dirigido
        :rtype: float
        """
        return measure.cityblock( P1.obtener_coord(), 
                          P2.obtener_coord() )

    def minkowski(self, P1:punto, P2:punto)->float:
        """Regresa la distancia minkowski

        :param P1: Punto inicial
        :type P1: punto
        :param P2: Punto final
        :type P2: punto
        :return: Longitud del segmento dirigido
        :rtype: float
        """
        return measure.minkowski( P1.obtener_coord(), 
                          P2.obtener_coord() )

def obtener_n_triangulos(n, triangulos):
    for i in range(n):
        nuevos_triangulos= []
        for triangl in triangulos:
            nuevos_triangulos.extend( obtener_internos(  list( triangl.obtener_vertices() ) , i ) )
        triangulos= nuevos_triangulos[:]
    return triangulos
        
    
def obtener_internos(V, i):
    nuevos_triangulos= []
    for i in range( 3 ):
        aux_V= V[:]
        v= aux_V.pop( i )
        nuevos_triangulos.append( triangulo( v, segmento( v,aux_V[0] ).obtener_punto_medio(), segmento( v, aux_V[1] ).obtener_punto_medio() ) )
    return nuevos_triangulos
    
    
