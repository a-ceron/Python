class triangulo( object ):
    def __init__(self, a, b, c):
        self.A= a
        self.B= b
        self.C= c
        
    def obtener_aristas(self):
        return segmento( self.A, self.B ), segmento( self.A, self.C ), segmento( self.C, self.B )
    
    def dibuja(self,relleno):
        fill(relleno)
        triangle( self.A.obtener_x(),self.A.obtener_y(),
                 self.B.obtener_x(),self.B.obtener_y(),
                 self.C.obtener_x(),self.C.obtener_y() )
        
    def obtener_vertices(self):
        return self.A, self.B, self.C
                 
class segmento( object ):
    def __init__(self, A, B ):
        self.x0= A
        self.xf= B
        
    def distancia(self):
        return sqrt( (self.x0.obtener_x() - self.xf.obtener_x())**2 + (self.x0.obtener_y() - self.xf.obtener_y())**2 )
    
    def obtener_punto_medio(self):
        x= (self.xf.obtener_x() + self.x0.obtener_x())/2
        y= (self.xf.obtener_y() + self.x0.obtener_y())/2
        return coord( x, y )
    
    def obtener_punto_ini(self):
        return self.x0
    
    def obtener_punto_fin(self):
        return self.xf
    
    
class coord( object ):    
    def __init__( self, x, y ): 
        self.x= x
        self.y= y
        
    def obtener_x(self):
        return self.x
    
    def obtener_y(self):
        return self.y
    
    def obtener_coord(self):
        return( self.obtener_x(), self.obtener_y() )
    
    def fijar_x(self,x):
        self.x= x
    
    def fijar_y(self,y):
        self.y= y
    
from itertools import permutations
    
####################
x= 480 
y= 320

def setup():
    size(x, y)


    
def draw():
    varios(7)
        
def varios(n):
    V1, V2, V3= coord(20,y-20), coord(x-20,y-20), coord((x-20)/2,20)
    triangulos= [ triangulo( V1, V2, V3 ) ]
    
    for i in range(n):
        nuevos_triangulos= []
        for triangl in triangulos:
            nuevos_triangulos.extend( obtener_internos(  list( triangl.obtener_vertices() ) , i ) )
        triangulos= nuevos_triangulos[:]
        
    dibujar( triangulos )
        
def dibujar(triangulos):    
    for triangl in triangulos:
        triangl.dibuja(0) 
    
    
def obtener_internos(V, i):
    nuevos_triangulos= []
    for i in range( 3 ):
        aux_V= V[:]
        v= aux_V.pop( i )
        
        nuevos_triangulos.append( triangulo( v, segmento( v,aux_V[0] ).obtener_punto_medio(), segmento( v, aux_V[1] ).obtener_punto_medio() ) )
        
    return nuevos_triangulos
    
    
