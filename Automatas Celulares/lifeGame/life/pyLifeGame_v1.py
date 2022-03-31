"""
Juego de la vida.
    Ariel Cerón González

Para la materia de Introducción a la Modelación de Sistemas Complejos con Autómatas Celulares.

Maestria en Ciencias e Ingienería de la Computación (IA)
    UNAM, 2022.

Released under the GNU General Public License
"""
VERSION= "0.1"

try:
    #----SO
    ##################
    import sys 
    

    #----Gráficos
    ##################
    import pygame as pg
    import pygame_gui

    #----Procesamiento
    ##################
    import numpy as np
    from pygame.locals import QUIT

except ImportError as err:
    print( f"Algunos módulos no se pudieron cargar. {err}")
    sys.exit(2)

#---Estilos
class Colores():
    negro= (0,0,0)
    blanco= (255,255,255)
    verde= (0, 255, 0)
    azul= (255, 0, 0)
    rojo= (0, 0, 255)
    gainsboro= (220,220,220)
    aqua= (25,252,241)

#---Objetos del juego
class Celula():
    """Célula que se encuentra en el juego"""

    def __init__(self, pos, estado:int=1, ) -> None:
        """Constructor"""
        self.estado= estado
        self.vecinos= []
        self.pos= pos 

    def obtener_pos(self)->int:
        return self.pos

    def obtener_vecinos(self)->list:
        return self.vecinos

    def asignar_vecinos(self, vecinos:list)->None:
        self.vecinos= vecinos

    def obtener_estado(self)->int:
        """Regresa el estado actual de la célula

        :return: Estado de la célula
        :rtype: int
        """
        return self.estado
    
    def asignar_estado(self, estado:int)->None:
        """Asigna un nuevo estado a la célula

        :param estado: Nuevo estado de la célula
        :type estado: int
        """
        self.estado= estado

    def obtener_vecinos_vivos(self, estados)->int:
        """Obtiene el número de vecinos vivos"""
        #e_vecinos= [ espacio[i][0].obtener_estado() for i in self.vecinos ]
        v_estados= [ estados[i] for i in self.vecinos ]
        return sum( v_estados )
    
    def actualizar(self):
        """Actualiza el estado de la célula"""
        pass
    
    def obtener_color(self):
        return Colores.blanco if self.obtener_estado() else Colores.negro

class Vida():
    """Inicia un nuevo juego de la vida
    """
    def __init__(self, size, g_size)->None:
        """Constructor"""
        self.__crear_celulas(size, g_size)
        self.__asignar_vecinos()
        
    def __crear_celulas(self, size, g_size):
        juego_pos, juego_size, _, _= obtener_configuracion( size )

        self.n_rows= int(( juego_size[0] - juego_pos[0] ) / g_size)
        self.n_cols= int(( juego_size[1] - juego_pos[1] ) / g_size)

        self.celulas= {}
        i= 0
        for x in range(int(juego_pos[0]), int(juego_size[0]), g_size):
            for y in range(int(juego_pos[1]), int(juego_size[1]), g_size):
                self.celulas[ i ]=  [Celula(i), x,y,g_size ] 
                i+= 1

    def __asignar_vecinos(self):
        for contenedor in self.celulas.values():
            pos= contenedor[0].obtener_pos()
            vecinos=[]

            vecinos.append( ( pos - self.n_rows ) - 1 )
            vecinos.append( ( pos - self.n_rows ) )
            vecinos.append( ( pos - self.n_rows ) + 1 )

            vecinos.append(  pos - 1 )
            vecinos.append(  pos - 2 )

            vecinos.append( ( pos + self.n_rows ) - 1 )
            vecinos.append( ( pos + self.n_rows ) )
            vecinos.append( ( pos + self.n_rows ) + 1 )

            index= []
            for i in range( len(vecinos) ):
                if( ( vecinos[i] > 0 ) and ( vecinos[i] < self.n_rows * self.n_cols ) ):
                    index.append( i )
            vecinos= [vecinos[i] for i in index]


            contenedor[0].asignar_vecinos( vecinos )

    def info(self):
        print("Juego de la vida v0.1")
        print(" Tamaño de la malla", (self.n_rows,self.n_cols))
        print("Visualización:")
        print( self.obtener_estado() )

    def obtener_malla(self):
        return self.celulas

    def obtener_estado(self):
        estado= []
        for i in range( self.n_cols ):
            filas= []
            for j in range( self.n_rows ):
                filas.append( self.celulas[ j + i*self.n_rows ][0].obtener_estado() )
            estado.append( filas )
        return np.matrix( estado )

    def nueva( self, pantalla):
        for value in self.celulas.values():
            rect = pg.Rect( value[1], value[2], value[3]-0.1, value[3]-0.1 )
            color= Colores.aqua if not value[0].obtener_estado() else Colores.negro
            pg.draw.rect(pantalla, color, rect)

    def obtener_estado_act(self):
        return [ elemento[0].obtener_estado() for elemento in self.celulas.values() ]

    def generar_estados(self):
        estado_nvo= []
        for celula in self.celulas.values():
            estado_nvo.append( np.random.randint(0,2) )                             
        for i in range( len( estado_nvo ) ):
            self.celulas[i][0].asignar_estado( estado_nvo[i] )

    def actualizar(self, pantalla):
        estado_act= self.obtener_estado_act()

        estado_nvo= []
        for celula in self.celulas.values():
            estado_nvo.append( obtener_nuevo_estado(
                                   celula[0].obtener_estado(),
                                   celula[0].obtener_vecinos_vivos( estado_act ) 
                                ) 
                            )
        for i in range( len( estado_nvo ) ):
            self.celulas[i][0].asignar_estado( estado_nvo[i] )

        #self.nueva( pantalla )
        #print(self.obtener_estado())
#---Funciones del juego
def obtener_nuevo_estado( estado, n_vecinos:int ) -> int:
    """Reglas de la vida

    :param n_vecinos: Número de vecinos vivos
    :type n_vecinos: int
    :return: Estado en función de los vecinos vivos
    :rtype: int
    """

    #return 1 if ( ( n_vecinos >= 2 ) and ( n_vecinos <= 3 ) ) else 0
    if( estado ):
        return 1 if n_vecinos == 2 or n_vecinos == 3 else 0
    else:
        return 1 if n_vecinos == 3 else 0


#---Desarrollo del juego
def play( size:tuple=(800,500), g_size= 20 ):
    """Función principal del juego de la vida

    :param size: Tamño de la pantalla principal, defaults to (800,500)
    :type size: tuple, optional
    """

    #Inicio del entorno
    pg.init()

    #Iniciamos el juego de la vida
    vida= Vida( size, g_size )

    #Configuraciones del juego
    pantalla, fondo, manager= configurar_juego( size )
    nuevo, aleatorio, iniciar= configurar_botones( size, manager )
    dibujar_gui( size, g_size, pantalla, vida.obtener_malla() )

    #Funciones por hacer
    vida.nueva( pantalla )
    

    clock = pg.time.Clock()
    fg= 1

    en_ejecucion= True
    while( en_ejecucion ):
        time_delta = clock.tick( fg )
        for event in pg.event.get():
            if( event.type == QUIT ):
                en_ejecucion= False
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
              if event.ui_element == aleatorio:
                vida.generar_estados()
            manager.process_events(event)

        
        actualizar(manager, time_delta, pantalla, fondo,size)
        vida.actualizar( pantalla )
        #vida.actualizar()
        pg.display.update()

    pg.quit()

def actualizar(manager, time_delta, pantalla,fondo,size):
    manager.update(time_delta)
    #pantalla.blit(fondo, (0, 0))
    #dibujar_gui(size, pantalla)
    manager.draw_ui(pantalla)

def obtener_configuracion(size):
    #Margenes de los contenederos y espacio entre ellos
    v_margen= 10; h_margen= 10; gap= 5
    
    #Calculamos los tamaños de la pantalla que sobran
    v_espacio= size[1] - ( 2 * v_margen )
    h_espacio= size[0] - ( ( 2 * h_margen ) + gap )
    
    #Generamos las posiciones
    juego_pos= (h_margen, v_margen)
    juego_size= ( h_espacio * 0.75, v_espacio )

    botonera_pos= ( h_espacio * 0.78 + gap , v_margen )
    botonera_size= ( h_espacio * 0.23, v_espacio )

    return juego_pos, juego_size, botonera_pos, botonera_size

def dibujar_gui(size,g_size, pantalla, vida):
    #Obtenemos posiciones y tamaños
    juego_pos, juego_size, botonera_pos, botonera_size= obtener_configuracion( size )

    #Graficamos 
    pg.draw.rect( pantalla, Colores.negro, pg.Rect( juego_pos, juego_size ) )
    pg.draw.rect( pantalla, Colores.aqua, pg.Rect( botonera_pos, botonera_size ) )
    

def dibujar_malla( pantalla, malla:dict ):
    for values in malla.values():
        rect = pg.Rect( values[1], values[2], values[3], values[3] )
        pg.draw.rect(pantalla, Colores.aqua , rect, 1)

# def dibujar_malla( juego_pos, juego_size, g_size, pantalla ):
#     for x in range(int(juego_pos[0]), int(juego_size[0]), g_size):
#         for y in range(int(juego_pos[1]), int(juego_size[1]), g_size):
#             rect = pg.Rect(x, y, g_size, g_size)
#             pg.draw.rect(pantalla, Colores.aqua , rect, 1)
  
def configurar_juego( size ):
    #Configuración del entorono
    pg.display.set_caption('Juego de la vida')
    pantalla = pg.display.set_mode( size )

    fondo = pg.Surface( size )
    fondo.fill(Colores.blanco)

    #Inicio de un GUI para añadir botones
    manager = pygame_gui.UIManager( size )

    return pantalla, fondo, manager

def configurar_botones( size, manager ):
    _, _, botonera_pos, botonera_size= obtener_configuracion( size )
    #Botones

    v_espacio= botonera_size[1]*0.01; h_espacio= botonera_size[1]*0.05
    b_size= (botonera_size[0]*0.8, botonera_size[1]*0.1) 
    x_pos= botonera_pos[0] + 3*v_espacio
    y_pos= botonera_pos[1] + h_espacio

    nuevo = pygame_gui.elements.UIButton(
                relative_rect=pg.Rect( (x_pos, y_pos), b_size ),
                text='Limpiar',
                manager=manager)
    aleatorio = pygame_gui.elements.UIButton(
                relative_rect=pg.Rect( (x_pos, y_pos + 2.5*h_espacio ), b_size ),
                text='Random',
                manager=manager)
    iniciar = pygame_gui.elements.UIButton(
                relative_rect=pg.Rect( (x_pos, y_pos + 15*h_espacio), b_size ),
                text='Iniciar',
                manager=manager)

    return nuevo, aleatorio, iniciar

    
    