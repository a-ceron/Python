# PyGame

## Pantalla inicial
Primero debemos empezar a generar el entorno, donde el juego será desarrollado
```python
import pygame

pygame.init()
```
El entorno ya inicio, pero debe acabar o la memoria de nuestro dispositivo puede colapsar por tener tantos procesos que no son usados
```python
pygame.quit()
```
Ya iniciamos y terminamos nuestro entorno, ahora viene la parte de desarrollo.

Una de los primeros elementos que configure es el de la pantalla, defini el tamaño de la pantalla, el nombre de la ventana y el fondo.
```python
screen= pygame.display.set_mode( size )
pygame.display.set_caption('Basic Pygame program')

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((250, 250, 250))
```
Para poder observar los resultados los vamos a mostrar en pantalla. Sin embargo, cada tiempo mostramos solo un evento, así que mostraremos una infinidad de eventos en un ciclo while y además agregaremos una condición de paro, para tener el control del juego
```python
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            return

    screen.blit(background, (0, 0))
    pygame.display.flip()
```

Todos los elementos que usaremos en pyGame son iniciados de forma general al iniciar nuestro entorno, por ello podemos llamarlos y configurarlos pero sin iniciarlos.

#### Blitting
Blitting es un termino usado en pyGame para refererice a un renderizado. En el ejemplo se uso el método *blit* para renderizar la pantalla (screen) con un nuevo fondo.

Blitting es una operación lenta, por lo que se debe tener cuidado al usar esta función

## Estrucutura del juego

En la documentación de pyGame se recomienda hacer una programación POO para el desarrollo del juego y una función main que contenga las configuraciónes del juego en una función y dentro de ella hacer la lógica del juego llamando a los objetos construidos