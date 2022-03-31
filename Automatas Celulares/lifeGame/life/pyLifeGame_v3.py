"""
Juego de la vida.
    Ariel Cerón González

Para la materia de Introducción a la Modelación de Sistemas Complejos con Autómatas Celulares.

Maestria en Ciencias e Ingienería de la Computación (IA)
    UNAM, 2022.

Released under the GNU General Public License
"""
VERSION= "0.3"

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
    from random import random
    from math import floor
    from time import sleep

except ImportError as err:
    print( f"Algunos módulos no se pudieron cargar. {err}")
    sys.exit(2)

#---Estilos
class Colores():
    negro= (0,0,0)
    blanco= (255,255,255)
    verde= (0, 255, 0)
    rojo= (255, 0, 0)
    azul= (0, 0, 255)
    gainsboro= (220,220,220)
    aqua= (25,252,241)

#---Objetos
class Entorno():
    """Entorno del juego"""
    def __init__(self,pos:tuple, dim:tuple, n_rows:int, n_cols:int ) -> None:
        """Constructor"""
        self.pos= pos
        self.dim= dim
        self.n_rows= n_rows
        self.n_cols= n_cols
        self.dimCW= self.dim[0]/ self.n_rows
        self.dimCH= self.dim[1]/ self.n_cols
        self.__generar_entorno()
        self.colores= [Colores.aqua, Colores.negro, Colores.blanco]

    def __dibujar_fondo(self, screen):
        """Dibuja el fondo del área del juego

        :param screen: Pantalla donde se desarrolla el juego
        :type screen: _type_
        """
        game= pg.Rect( self.pos[0], self.pos[1], self.dim[0], self.dim[1] )
        pg.draw.rect( screen, Colores.aqua, game )

    def __generar_entorno(self):
        """Genera a las celulas del entorno"""
        self.asignar_celulas ( np.zeros((self.n_rows, self.n_cols)) )
        self.__generar_posiciones()

    def __generar_posiciones(self):
        """Genera una lista de posiciones de las celulas"""
        self.x_pos= [self.pos[0] + self.dimCW* i for i in range(self.n_rows)]
        self.y_pos= [self.pos[1] + self.dimCH* i for i in range(self.n_cols)]
        

    def obtener_celulas(self):
        """Regresa las celulas del entorno"""
        return self.celulas
    
    def asignar_celulas(self,celulas):
        """Asigna las celulas del entorno"""
        self.celulas= celulas

    def asignar_estado(self, pos:tuple, estado=None):
        """Asigna un estado a una célula

        :param pos: Posición de la celula en la pantalla
        :type pos: tuple
        :param estado: Estado a asignar, defaults to None
        :type estado: _type_, optional
        """        """"""
        #Limites del área del juego
        if( pos[0] > self.pos[0]+ self.dim[0] or pos[1] > self.pos[1] + self.dim[1] or pos[0] < self.pos[0] or pos[1] < self.pos[1] ):
            return

        pos= self.screenxy_a_celulaxy( pos)

        celulas= self.obtener_celulas()
        celulas[pos]= 0 if celulas[pos] else 1
        
    def screenxy_a_celulaxy(self, screenXY:tuple ) -> tuple:
        #Transformacion de posición en pantalla a posición en matriz
        posX= int( floor( screenXY[0] / self.dimCW ) )
        posY= int( floor( screenXY[1] / self.dimCH ) )
        return (posX, posY)

    def dibujar(self, screen):
        """Dibuja los estados de las celulas en el entorno

        :param screen: Entorno del juego
        :type screen: _type_
        """
        self.__dibujar_fondo( screen )

        celulas= self.obtener_celulas()

        for y in self.y_pos:
            for x in self.x_pos:
                rect= pg.Rect(x, y, self.dimCW, self.dimCH)
                pos= self.screenxy_a_celulaxy( (x,y) )
                pg.draw.rect(screen, self.colores[ 0 if celulas[pos] else 1], rect, 1 if celulas[pos] else 0)
                
        
    def evolucionar(self):
        """Evoluciona el entorno"""
        gameState= self.obtener_celulas()
        newGameState= np.copy( gameState )
        for y in range(0, self.n_cols):
            for x in range (0, self.n_cols):
                # Calculamos el número de vecinos cercanos.
                n_neigh =   gameState[(x - 1) % self.n_rows, (y - 1)  % self.n_cols] + \
                            gameState[(x)     % self.n_rows, (y - 1)  % self.n_cols] + \
                            gameState[(x + 1) % self.n_rows, (y - 1)  % self.n_cols] + \
                            gameState[(x - 1) % self.n_rows, (y)      % self.n_cols] + \
                            gameState[(x + 1) % self.n_rows, (y)      % self.n_cols] + \
                            gameState[(x - 1) % self.n_rows, (y + 1)  % self.n_cols] + \
                            gameState[(x)     % self.n_rows, (y + 1)  % self.n_cols] + \
                            gameState[(x + 1) % self.n_rows, (y + 1)  % self.n_cols]
                # Regla #1 : Una celda muerta con exactamente 3 vecinas vivas, "revive".
                if gameState[x, y] == 0 and n_neigh == 3:
                    newGameState[x, y] = 1
                # Regla #2 : Una celda viva con menos de 2 o 3 vecinas vinas, "muere".
                elif gameState[x, y] == 1 and (n_neigh < 2 or n_neigh > 3):
                    newGameState[x, y] = 0 
        self.asignar_celulas( newGameState )

    def aplicar_reglas(self, estado, n_vecinos:int ) -> int:
        """Reglas de la vida

        :param n_vecinos: Número de vecinos vivos
        :type n_vecinos: int
        :return: Estado en función de los vecinos vivos
        :rtype: int
        """
        print(estado, n_vecinos)
        if( estado ):
            return 1 if n_vecinos == 2 or n_vecinos == 3 else 0
        else:
            return 1 if n_vecinos == 3 else 0
 
    def matar_celulas(self):
        self.asignar_celulas( np.zeros((self.n_rows, self.n_cols)) )

    def estados_aleatorios(self):
        self.asignar_celulas( np.random.randint(2, size=(self.n_rows, self.n_cols)) )


#---Juego
def jugar( window:tuple= (800,500) ):
    """
        Juego de la vida.
    """
    #Inicio del entorno
    pg.init()

    pantalla= configurar_pantalla(window=window)

    manager= pygame_gui.UIManager( window )
    env, botones= configurar_gui( window, pantalla, manager )

    clock = pg.time.Clock()
    fg= 60
    
    env.dibujar(pantalla)

    en_ejecucion= True
    inicio= False
    env.estados_aleatorios()

    while( en_ejecucion ):
        time_delta = clock.tick( fg )

        en_ejecucion, inicio= verificar_eventos( botones, manager, env, [en_ejecucion, inicio])

        env.dibujar(pantalla)
        if( inicio ):
            env.evolucionar() 

        manager.update(time_delta)
        manager.draw_ui(pantalla)
        pg.display.update()
    
    pg.quit()

def verificar_eventos(botones, manager, env, flags):
    for event in pg.event.get():
        if( event.type == QUIT ):
            flags[0]= False
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == botones[0]:
                env.matar_celulas()
            elif event.ui_element == botones[1]:
                env.estados_aleatorios()
            elif( event.ui_element == botones[2] ):
                if( botones[2].text == "Pausa" ):
                    botones[2].set_text("Iniciar")
                    flags[1]= False
                else:
                    botones[2].set_text( "Pausa" )
                    flags[1]= True
        if pg.mouse.get_pressed()[0]:
            pos= pg.mouse.get_pos()
            env.asignar_estado( pos )
        manager.process_events(event)

    return flags[0], flags[1]

def configurar_pantalla(caption:str= "Juego de la vida", window:tuple= (800,500), fill:Colores= Colores.blanco):
    #Configuramos los parámetros de la ventana
    pg.display.set_caption( caption ) 
    pantalla= pg.display.set_mode( window )
    pantalla.fill( fill )

    return pantalla

def configurar_gui( window:tuple, pantalla,manager ):
    #Configuramos el diseño del entorno para verlo mejor
    return gui_game( window, pantalla ),gui_cont_botones( window, pantalla, manager )
    
def gui_game( window:tuple, pantalla ):
    w_game= 0.8*window[0]; h_game= 0.95*window[1]
    x_game= 0.01*window[0]; y_game= 0.02*window[1]
    game= pg.Rect( x_game, y_game, w_game, h_game )
    pg.draw.rect( pantalla, Colores.negro, game )
    return Entorno( (x_game,y_game), (w_game,h_game), 40, 40 )

def gui_cont_botones( window:tuple, pantalla, manager ):
    w_botones= 0.17*window[0]; h_botones= 0.95*window[1]
    x_botones= 0.82*window[0]; y_botones= 0.02*window[1]
    botones= pg.Rect( x_botones, y_botones, w_botones, h_botones)
    pg.draw.rect( pantalla, Colores.negro, botones )

    return gui_botones( (x_botones, y_botones), (w_botones,h_botones), manager )

def gui_botones( pos:tuple, dim:tuple, manager ):
    v_espacio= dim[1]*0.01; h_espacio= dim[1]*0.05
    b_size= (dim[0]*0.8, dim[1]*0.1) 
    x_pos= pos[0] + 3*v_espacio
    y_pos= pos[1] + h_espacio

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

