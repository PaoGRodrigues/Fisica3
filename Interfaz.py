#Librerias importadas
from GasesIdeales import *
from GraficadorIsotermas import *
#import os

from tkinter import *
from tkinter import ttk

# La clase 'Aplicacion' ha crecido. En el ejemplo se incluyen
# nuevos widgets en el método constructor __init__(): Uno de
# ellos es el botón 'Info'  que cuando sea presionado llamará 
# al método 'verinfo' para mostrar información en el otro 
# widget, una caja de texto: un evento ejecuta una acción: 

def ventanaGasesIdeales():

		ventana1 = Toplevel()
		ventana1.geometry('500x300')

		# Impide que los bordes puedan desplazarse para
		# ampliar o reducir el tamaño de la ventana 'self.ventana':
		
		ventana1.resizable(width=False,height=False)
		ventana1.title('Cálculo')
		
		# Define el widget Button 'self.bcalcular' que llamará 
		# al metodo 'self.verinfo' cuando sea presionado
		ventana1.lpresion = Label(ventana1, text = "Presión: ").place(x=100, y=30)
		vpresion = IntVar()
		ventana1.epresion = Entry(ventana1,textvariable = vpresion).place(x=200, y=30)

		ventana1.lvolumen = Label(ventana1, text = "Volumen: ").place(x=100, y=60)
		vvolumen = IntVar()
		ventana1.evolumen = Entry(ventana1, textvariable = vvolumen).place(x=200, y=60)

		ventana1.lmoles = Label(ventana1, text = "Moles: ").place(x=100, y=90)
		vmoles = IntVar()
		ventana1.emoles = Entry(ventana1, textvariable = vmoles).place(x=200, y=90)

		ventana1.ltemperatura = Label(ventana1, text = "Temperatura: ").place(x=100, y=120)
		vtemperatura = IntVar()
		ventana1.etemperatura = Entry(ventana1, textvariable = vtemperatura).place(x=200, y=120)

		ventana1.bcalcular = ttk.Button(ventana1, text='Calcular', 
								command=lambda: calcularGasesIdeales(vpresion.get(),vvolumen.get(),vmoles.get(),vtemperatura.get()))

		ventana1.bcalcular.pack(side=LEFT)

		resultado = calcularGasesIdeales(vpresion.get(),vvolumen.get(),vmoles.get(),vtemperatura.get())
		# Coloca el botón 'self.bcalcular' debajo y a la izquierda
		# del widget anterior
		
		ventana1.bsalir = ttk.Button(ventana1, text='Salir', 
								 command=ventana1.destroy)
								 
		# Coloca el botón 'self.bsalir' a la derecha del 
		# objeto anterior.
								 
		ventana1.bsalir.pack(side=RIGHT)
		
		# El foco de la aplicación se sitúa en el botón
		# 'self.bcalcular' resaltando su borde. Si se presiona
		# la barra espaciadora el botón que tiene el foco
		# será pulsado. El foco puede cambiar de un widget
		# a otro con la tecla tabulador [tab]
		
		ventana1.bcalcular.focus_set()
		ventana1.mainloop()	

##EVENTO del boton CALCULAR ########################################
def calcularGasesIdeales(presion,volumen,moles,temperatura):
	result = gases_ideales(presion, volumen, moles, temperatura)
	if(result == '-1'):
		print("No se puede imprimir")
	else:
		toplevel = Toplevel()
		toplevel.geometry('600x310')
		label1 = Label(toplevel, text = "Resultado: {0}".format(result)).place(x=25, y=25)
		return result

####################################################################

def ventanaIsotermas():
		
		ventana2 = Toplevel()
		ventana2.geometry('500x300')
		
		ventana2.resizable(width=True,height=True)
		ventana2.title('Isotermas')	
	
		###################################################################
		ventana2.lvolumen = Label(ventana2, text = "Volumen Máximo: ").place(x=100, y=120)
		vvolumen = IntVar()
		ventana2.evolumen = Entry(ventana2, textvariable = vvolumen).place(x=200, y=120)

		ventana2.ltemperatura1 = Label(ventana2, text = "Temperatura 1: ").place(x=100, y=30)
		vtemperatura1 = IntVar()
		ventana2.etemperatura1 = Entry(ventana2,textvariable = vtemperatura1).place(x=200, y=30)

		ventana2.ltemperatura2 = Label(ventana2, text = "Temperatura 2: ").place(x=100, y=60)
		vtemperatura2 = IntVar()
		ventana2.etemperatura2 = Entry(ventana2, textvariable = vtemperatura2).place(x=200, y=60)

		ventana2.ltemperatura3 = Label(ventana2, text = "Temperatura 3: ").place(x=100, y=90)
		vtemperatura3 = IntVar()
		ventana2.etemperatura3 = Entry(ventana2, textvariable = vtemperatura3).place(x=200, y=90)

		print(vtemperatura1.get())
		print(vtemperatura2.get())
		print(vtemperatura3.get())
		print(vvolumen.get())
		####################################################################
		ventana2.bcalcular = ttk.Button(ventana2, text='Graficar Isotermas', 
								command=lambda: graficar(vvolumen.get(), 1, vtemperatura1.get(),vtemperatura2.get(),vtemperatura3.get()))

		ventana2.bcalcular.pack(side=LEFT)
		ventana2.mainloop()

class Aplicacion():

	def __init__(self):
		self.raiz = Tk()
		self.raiz.geometry('400x400')
		
		self.raiz.resizable(width=True,height=True)
		self.raiz.title('Bienvenido')	
		
		#self.raiz.boton_gi = ttk.
		self.raiz.boton_gi = ttk.Button(self.raiz, text='Calcular Gases Ideales', 
								command=lambda:ventanaGasesIdeales()).place(x=150, y=200)

		#self.raiz.boton_gi.pack(side=LEFT)

		#self.raiz.boton_isot = ttk.
		self.raiz.boton_isot = ttk.Button(self.raiz, text='Graficar Isotermas', 
								command=lambda: ventanaIsotermas()).place(x=150, y=300)

		#self.raiz.boton_isot.pack(side=RIGHT)

			# Mostrar la ventana
		self.raiz.mainloop()		


def main():
	mi_app = Aplicacion()
	return 0

main()
