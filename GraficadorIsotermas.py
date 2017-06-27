from matplotlib import pyplot
from GasesIdeales import *

def graficar(volumen,moles, T1, T2, T3):
	# Valores del eje X que toma el gráfico.
	x = range(0, volumen)
	T = [T1,T2,T3]

	presionMax = 0
	# Graficar ambas funciones.
	for h in T:
		presion =[]
		for i in x:
			if i == 0:
				i=0.1
			actual = gases_ideales(0,i,moles,h)
			if(presionMax<actual[1]):
				presionMax = actual[1]
			presion.append(actual[1])
			#gases_ideales(0,i,moles,h)
		print(presion)
		pyplot.plot(x, presion)
	# Establecer el color de los ejes.
	pyplot.axhline(0, color="black")
	pyplot.axvline(0, color="black")
	# Limitar los valores de los ejes.	
	pyplot.xlim(0, volumen)
	pyplot.ylim(0, presionMax)
	pyplot.show()
