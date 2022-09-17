# Introudcción

Un algoritmo de aprendizaje de máquina (machine learning) es aquel que puede aprender de los datos. Esta definición es importante porque nos inicia en el camino de saber si puedo, o no, usar el aprendizaje de máquina en mi problema, pues la condición inicial es que haya datos, pero no solo eso, muchos de los algoritmos necesitan información verdadera, más adelante se entenderá esto por ahora entiendase que se debe tener información de la respuesta.

El primer modelo que se va a costruir es una neurona simple (yo creo que también se le puede llamar perceptron), la cual esta definida por la siguiente función
$$
\phi(X,W,b) = \phi(b + \sum w_i * x_i) = \phi( b + W^TX)
$$

Si ya tienes experiencia con la definición de funciones omite este parrafo, si tienes miedo de esta notación o aún te cuesta entender (a mi me costó mucho) dejame decirte que en realidad es muy fácil, $\phi(X,W,b)$ esta es una forma de decir que una función $\phi$ va a tomar tres variables en la entrada que se llaman $X,W,b$;  $\phi(b + \sum w_i * x_i)$ esta forma dice exactamente lo mismo pero acá te dice cómo operar a los elementos, es decir nos dice que para cada elemento $i$ de $X,W$ debemos sumarle un valor $b$; para la última notación, de nuevo nos explica cómo operar pero ahora nos lo resume en formac de operaciones matriciales y dice que podemos sumar los valores $b$ al resultado de operar la matriz transpuesta $W$ por el vector $X$.

Vamos a aprobechar de numpy para realizar las operaciones matriciales, pues esta librería esta optimizada para este tipo de operaciones y ninguna de nuestras implementaciones (usando python) va a superar su rendimiento. Si se observa la definiciín se parece mucho a la primera que hacemos
```python
def neurona(X,W,b,f):
    return f(b + W.T@X)
```