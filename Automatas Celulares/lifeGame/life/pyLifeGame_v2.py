"""
Juego de la vida.
    Ariel Cerón González

Para la materia de Introducción a la Modelación de Sistemas Complejos con Autómatas Celulares.

Maestria en Ciencias e Ingienería de la Computación (IA)
    UNAM, 2022.

Released under the GNU General Public License
"""

import secrets


VERSION= "0.2"

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
class Celula():
    """Célula que se encuentra en el juego"""

    def __init__(self, pos:int, estado:int=0 ) -> None:
        """Constructor"""
        self.estado= estado
        self.vecinos= []
        self.pos= pos

    def obtener_pos(self)->int:
        """Regresa la posición de la célula"""
        return self.pos

    def obtener_vecinos(self)->list:
        """Regresa una lista de celulas que hace referencia a cada vecino de la celula

        :return: Lista de celulas_
        :rtype: list
        """
        return self.vecinos

    def asignar_vecinos(self, vecinos:list)->None:
        """Asigna una lista de celulas que hace referencia a cada vecino de la celula

        :param vecinos: Lista de celulas_
        :type vecinos: list
        """
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
        print(self.pos)
        v_estados= [ vecino.obtener_estado() for vecino in estados ]
        return sum( v_estados )

    def obtener_color(self):
        """Regresa el color de la célula"""
        return Colores.negro if self.obtener_estado() else Colores.blanco

class entorno():
    """Entorno del juego"""
    def __init__(self,pos:tuple, dim:tuple, n_rows:int, n_cols:int ) -> None:
        """Constructor"""
        self.pos= pos
        self.dim= dim
        self.n_rows= n_rows
        self.n_cols= n_cols
        self.dimCW= self.dim[0]/ self.n_cols
        self.dimCH= self.dim[1]/ self.n_rows
        self.__generar_entorno()

    def __dibujar_fondo(self, screen):
        """Dibuja el fondo del área del juego

        :param screen: Pantalla donde se desarrolla el juego
        :type screen: _type_
        """
        game= pg.Rect( self.pos[0], self.pos[1], self.dim[0], self.dim[1] )
        pg.draw.rect( screen, Colores.aqua, game )

    def __generar_entorno(self):
        """Genera a las celulas del entorno"""
        self.asignar_celulas ( [ Celula(i) for i in range( self.n_cols * self.n_rows) ] )
        print("Vecinos asignados")
        self.__asignar_vecinos()
        print(self.obtener_vecinos())
        self.__generar_posiciones()

    def __generar_posiciones(self):
        """Genera una lista de posiciones de las celulas"""
        self.y_pos= [self.pos[1] + self.dimCH* i for i in range(self.n_rows)]
        self.x_pos= [self.pos[0] + self.dimCW* i for i in range(self.n_cols)]

    def __asignar_vecinos(self):
        """Asigna vecinos a cada célula"""
        print("Asignando vecinos")
        celulas= self.obtener_celulas()
        for celula in celulas:
            pos= celula.obtener_pos()
            idx_vecinos=[]
            print("Posicion: ", pos)

            idx_vecinos.append( ( pos - self.n_rows ) - 1 )
            idx_vecinos.append( ( pos - self.n_rows ) )
            idx_vecinos.append( ( pos - self.n_rows ) + 1 )

            idx_vecinos.append(  pos - 1 )
            idx_vecinos.append(  pos + 1 )

            idx_vecinos.append( ( pos + self.n_rows ) - 1 )
            idx_vecinos.append( ( pos + self.n_rows ) )
            idx_vecinos.append( ( pos + self.n_rows ) + 1 )

            print("Vecinos: ", idx_vecinos)

            index= []
            for vecino in idx_vecinos:
                if vecino >= 0 and vecino < len(self.celulas):
                    index.append( idx_vecinos.index(vecino) )
            idx_vecinos= [idx_vecinos[i] for i in index]

            print("Vecinos finales: ", idx_vecinos)

            celula.asignar_vecinos( [celulas[i] for i in idx_vecinos] )

    def obtener_celulas(self):
        """Regresa las celulas del entorno"""
        return self.celulas
    
    def asignar_celulas(self,celulas):
        """Asigna las celulas del entorno"""
        self.celulas= celulas

    def asignar_estado(self, pos:tuple, estado=None):
        """Asigna un estado a una célula

        :param pos: Posición de la celula
        :type pos: tuple
        :param estado: Estado a asignar, defaults to None
        :type estado: _type_, optional
        """        """"""
        #Limites
        if( pos[0] > self.pos[0]+ self.dim[0] or pos[1] > self.pos[1] + self.dim[1] or pos[0] < self.pos[0] or pos[1] < self.pos[1] ):
            return

        #Transformacion
        posX= int(floor(pos[0]/self.dimCW))
        posY= int(floor(pos[1]/self.dimCH))
        pos= posX + posY * self.n_cols
        
        celulas= self.obtener_celulas()
        estado= 1 if celulas[pos].obtener_estado() == 0 else 0
        celulas[pos].asignar_estado(estado)
        
    def dibujar(self, screen):
        """Dibuja los estados de las celulas en el entorno

        :param screen: Entorno del juego
        :type screen: _type_
        """
        self.__dibujar_fondo( screen )

        celulas= self.obtener_celulas()
        i= 0

        for y in self.y_pos:
            for x in self.x_pos:
                rect= pg.Rect(x, y, self.dimCW, self.dimCH)
                pg.draw.rect(screen, 
                            celulas[ i ].obtener_color(),
                            rect, 
                            0 if celulas[ i ].obtener_estado() else 1)
                i+= 1
        
    def evolucionar(self):
        """Evoluciona el entorno"""
        viejo_estado= self.obtener_celulas()
        print( [ celula.obtener_estado() for celula in viejo_estado])
        nuevo_estado= [
            Celula( celula.obtener_pos(), self.aplicar_reglas( celula.obtener_estado(), celula.obtener_vecinos_vivos(viejo_estado) ) )for celula in viejo_estado
        ]
        print( [ celula.obtener_estado() for celula in nuevo_estado] )
        self.asignar_celulas( nuevo_estado )
         
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
        viejo_estado= self.obtener_celulas()
        nuevo_estado= [ Celula( celula.obtener_pos(), 0 ) for celula in viejo_estado]
            
        self.asignar_celulas( nuevo_estado )

    def estados_aleatorios(self):
        viejo_estado= self.obtener_celulas()
        nuevo_estado= [ 
            Celula( celula.obtener_pos(), 1 if round(random()) else 0 )for celula in viejo_estado ]
            
        self.asignar_celulas( nuevo_estado )

    def obtener_estados(self):
        estados= [ celula.obtener_estado() for celula in self.obtener_celulas() ]
        return np.array(estados).reshape(self.n_rows,self.n_cols)

    def obtener_vecinos(self):
        vecinos= [ len(celula.obtener_vecinos()) for celula in self.obtener_celulas() ]
        print(vecinos)
        return np.array(vecinos).reshape(self.n_rows,self.n_cols)

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
    fg= 1
    
    env.dibujar(pantalla)

    en_ejecucion= True
    inicio= False
    env.estados_aleatorios()

    while( en_ejecucion ):
        time_delta = clock.tick( fg )

        en_ejecucion, inicio= verificar_eventos( botones, manager, env, [en_ejecucion, inicio])

        print("Estados")
        print(env.obtener_estados())
        print("Vecinos")
        print(env.obtener_vecinos())
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
    return entorno( (x_game,y_game), (w_game,h_game), 5, 5 )

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

