#Librerias importadas
from GasesIdeales import *
from GraficadorIsotermas import *
from PrimerPrincipio import *

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

	####################################################################
		ventana2.bcalcular = ttk.Button(ventana2, text='Graficar Isotermas', 
								command=lambda: graficar(vvolumen.get(), 1, vtemperatura1.get(),vtemperatura2.get(),vtemperatura3.get()))

		ventana2.bcalcular.pack(side=LEFT)
		ventana2.mainloop()

###################################################################

def ventanaPP():
		
		ventana3 = Toplevel()
		ventana3.geometry('500x300')
		
		ventana3.resizable(width=True,height=True)
		ventana3.title('Isotermas')	
	
		###################################################################
		ventana3.lenergia = Label(ventana3, text = "Energía Interna: ").place(x=100, y=30)
		venergia = IntVar()
		ventana3.eenergia = Entry(ventana3, textvariable = venergia).place(x=200, y=30)

		ventana3.ltrabajo = Label(ventana3, text = "Trabajo: ").place(x=100, y=60)
		vtrabajo = IntVar()
		ventana3.etrabajo = Entry(ventana3, textvariable = vtrabajo).place(x=200, y=60)

		ventana3.lcalor = Label(ventana3, text = "Calor: ").place(x=100, y=90)
		vcalor = IntVar()
		ventana3.ecalor = Entry(ventana3, textvariable = vcalor).place(x=200, y=90)

	####################################################################
		ventana3.bcalcular = ttk.Button(ventana3, text='Graficar Isotermas', 
								command=lambda: calcularFormula(venergia.get(),vcalor.get(),vtrabajo.get()))

		ventana3.bcalcular.pack(side=LEFT)
		ventana3.mainloop()

##EVENTO del boton CALCULAR del Primer Princ ########################################
def calcularFormula(U, Q, W):
	result = formula(U,Q,W)
	if(result == '-1'):
		print("No se puede imprimir")
	else:
		toplevel = Toplevel()
		toplevel.geometry('600x310')
		label1 = Label(toplevel, text = "Resultado: {0}".format(result)).place(x=25, y=25)
		return result


class Aplicacion():

	def __init__(self):
		self.raiz = Tk()
		self.raiz.geometry('400x400')
		
		self.raiz.resizable(width=True,height=True)
		self.raiz.title('Bienvenido')	

		####################################################################
		self.raiz.boton_gi = ttk.Button(self.raiz, text='Calcular Gases Ideales', 
								command=lambda:ventanaGasesIdeales()).place(x=50, y=50)
		#self.raiz.boton_gi.grid(row=3,column=2)

		self.raiz.boton_isot = ttk.Button(self.raiz, text='Graficar Isotermas', 
								command=lambda: ventanaIsotermas()).place(x=50, y=150)
		#self.raiz.boton_isot.grid(row=4,column=2)


		self.raiz.boton_pp = ttk.Button(self.raiz, text='Primer Principio de Termodinámica', 
								command=lambda: ventanaPP()).place(x=50, y=300)
		#self.raiz.boton_pp.grid(row=6,column=2)

		####################################################################
			# Mostrar la ventana
		self.raiz.mainloop()		


def main():
	mi_app = Aplicacion()
	return 0

main()

