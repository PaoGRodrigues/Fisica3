#Animate

import numpy as np
from matplotlib import pyplot
from GasesIdeales import *

def graficar(volumen, volumenMax, moles, T1, T2, T3):
	# Valores del eje X que toma el gráfico.
	#NUMPY.ARANGE(Inicio, final, step, tipoDeDato)
	if((volumenMax>volumen) and (T1>0) and (T2>0) and (T3>0)):
		x = np.arange(0.1, volumenMax, 0.01, dtype=float)
		Temp = [T1,T2,T3]

		presionMax = 0

		puntoPresion = presion(volumen,moles,T1)[1]

		for h in Temp:
			pres =[]
			for i in x:
				#print(i)
				actual = presion(i,moles,h)
				#print(actual)
				pres.append(actual[1])

			pyplot.plot(x, pres)

		DATA = ((volumen,puntoPresion))
		point = pyplot.subplot()
		(x, y) = zip(DATA)
		point.plot(x, y, marker='o')
		#pyplot.plot(volumen, puntoPresion, color='m' ,marker='*')
		# Establecer el color de los ejes.
		pyplot.axhline(0, color="black")
		pyplot.axvline(0, color="black")
		# Limitar los valores de los ejes.	
		pyplot.xlim(0, volumenMax)
		pyplot.ylim(0, 100)
		pyplot.show()
