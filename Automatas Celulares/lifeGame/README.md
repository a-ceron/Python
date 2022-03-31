# El juego de la vida
---
## Introducción 
---
El juego de la vida es una autómata celular planteado por John Horton Conway en 1970. El desarrollo del juego es muy simple, hay un tablero dividido en celdas, cada celda puede tomar un estado: vivo o muerto; cada estado se define por la vecindad de la celda y un conjunto de reglas definidas por Conway.

La dinámica de las celdas, los patrónes, la facilidad de implementación y las diferentes propiedades que se han observado ( como el hecho de que es una máquina de Turing ) ha permitido el desarrollo de diferentes artículos en torno al juego de la vida.

## Reglas
---
El juego se desarrolla una malla 2-dimensional infinita, cuyos elementos se nombran celdas. Cada celda puede tomar 2 estados: vivo o muerto. Cada celda además, define su estado por la interacción de sus vecinos, para cada paso $t$ en el tiempo puede ocurrir:
1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
2. Any live cell with two or three live neighbours lives on to the next generation.
3. Any live cell with more than three live neighbours dies, as if by overpopulation.
4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

## Implementación
---
Es importante que antes de usar el juego se revise que se tenga la libreria pygame. En este trabajo se uso **pygame v2.1.1**
```bash
    git clone this.repo
    python main.py
```



# Referencias
[1] Wikipedia contributors. (2022, March 24). Conway's Game of Life. In Wikipedia, The Free Encyclopedia. Retrieved 17:54, March 24, 2022, from https://en.wikipedia.org/w/index.php?title=Conway%27s_Game_of_Life&oldid=1079031728