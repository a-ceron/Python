###############
#	MUESTREO Y ESTIMACIÓN DE DISTRIBUCIONES
#	Se hizo uso de una distribución normal para 
#	realizar el experimento, el siguiente paso es
#	buscar valores aleatorios para corroborar
#	en sistemas no controlados.
#
################
from scripts import obtener_valores, fpd, leer_datos, graficar_datos
from numpy.random import choice

L = 100
N = 100
UBICACION = "C:/Users/LVVV03781/Documents/Others/DeteccionAnomalias/codes/poblacion/datos/Poblacion_01.csv"

def graficas(plot=True):
	# Primer ejercicio con N= 1000
	n_10000 = obtener_valores(n=10000, path=UBICACION)

	# Segundo ejercico del vector de edades generado vamos a obtener una muestra aleatoria de tamaño 100 y de tamaño 1000
	n_100 = choice(n_10000, 100)
	n_1000 = choice(n_10000, 1000)

	#plot
	if plot:
		graficar_datos(leer_datos(UBICACION)['total'])
		fpd(n_10000, "Origen")
		fpd(n_100, "100 valores")
		fpd(n_1000, "1000 valores")

	return n_10000

def esperanza(valores:int)->int:
	"""Regresa el primer valor esperado"""
	return sum(valores)/len(valores)

def main():
	n_10000 = graficas()

	minimos = []
	maximos = []
	esperanzas = []
	for i in range(L):
		tmp = choice(n_10000, N)
		minimos.append(min(tmp))
		maximos.append(max(tmp))
		esperanzas.append(esperanza(tmp))

	fpd(minimos, "Minimos")
	fpd(maximos, "Maximos")
	fpd(esperanzas, "Esperanzas")
	

if __name__ == '__main__':
	main()
