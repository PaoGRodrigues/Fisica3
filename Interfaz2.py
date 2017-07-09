#Librerias importadas
from GasesIdeales import *
from GraficadorIsotermas import *

from tkinter import *
from tkinter import ttk

##EVENTO del boton CALCULAR ########################################
def imprimir(resultado, ventana):
	
	label1 = Label(ventana, text = "Resultado: {0}".format(resultado), font=("arial"), fg="blue", bg="white").place(x=150, y=250)
	return

####################################################################
def ventanaIsotermas(volumen,moles,tempOrig):
		
		ventana2 = Toplevel()
		ventana2.geometry('500x300')
		
		ventana2.resizable(width=True,height=True)
		ventana2.title('Isotermas')	
	
		###################################################################
		ventana2.lvolumen = Label(ventana2, text = "Volumen Máximo (lts): ").place(x=100, y=120)
		vvolumen = IntVar()
		ventana2.evolumen = Entry(ventana2, textvariable = vvolumen).place(x=250, y=120)

		ventana2.ltemperatura1 = Label(ventana2, text = "Temperatura 1 (K): ").place(x=100, y=60)
		vtemperatura1 = IntVar()
		ventana2.etemperatura1 = Entry(ventana2, textvariable = vtemperatura1).place(x=250, y=60)

		ventana2.ltemperatura2 = Label(ventana2, text = "Temperatura 2 (K): ").place(x=100, y=90)
		vtemperatura2 = IntVar()
		ventana2.etemperatura2 = Entry(ventana2, textvariable = vtemperatura2).place(x=250, y=90)

		ventana2.bgraficar = ttk.Button(ventana2, text='Graficar Isotermas', 
								command=lambda: graficar(volumen,vvolumen.get(),moles,tempOrig,vtemperatura1.get(),vtemperatura2.get()))

		ventana2.bgraficar.place(x=200, y = 200)
		ventana2.mainloop()

###################################################################
def ventanaPresion():

		ventana1 = Toplevel()
		ventana1.geometry('500x300')

		# Impide que los bordes puedan desplazarse para
		# ampliar o reducir el tamaño de la ventana 'self.ventana':
		
		ventana1.resizable(width=True,height=True)
		ventana1.title('Cálculo')
		
		
		# Define el widget Button 'self.bcalcular' que llamará 
		# al metodo 'self.verinfo' cuando sea presionado
		ventana1.lvolumen = Label(ventana1, text = "Volumen (lts): ").place(x=100, y=60)
		vvolumen = IntVar()
		ventana1.evolumen = Entry(ventana1, textvariable = vvolumen).place(x=250, y=60)

		ventana1.lmoles = Label(ventana1, text = "Moles: ").place(x=100, y=90)
		vmoles = IntVar()
		ventana1.emoles = Entry(ventana1, textvariable = vmoles).place(x=250, y=90)

		ventana1.ltemperatura = Label(ventana1, text = "Temperatura (K): ").place(x=100, y=120)
		vtemperatura = IntVar()
		ventana1.etemperatura = Entry(ventana1, textvariable = vtemperatura).place(x=250, y=120)

		#CALCULA RESULTADO
		#resultado = presion(vvolumen.get(),vmoles.get(),vtemperatura.get())
		ventana1.bcalcular = ttk.Button(ventana1, text='Calcular', 
								command=lambda:imprimir(presion(vvolumen.get(),vmoles.get(),vtemperatura.get()),ventana1))

		ventana1.bcalcular.place(x=50, y = 200)

		ventana1.bgraficar = ttk.Button(ventana1, text='Graficar', 
								command=lambda:ventanaIsotermas(vvolumen.get(),vmoles.get(),vtemperatura.get()))

		ventana1.bgraficar.place(x=200, y = 200)

		# Coloca el botón 'self.bcalcular' debajo y a la izquierda
		# del widget anterior
		
		ventana1.bsalir = ttk.Button(ventana1, text='Salir', 
								 command=ventana1.destroy)
								 
		# Coloca el botón 'self.bsalir' a la derecha del 
		# objeto anterior.
								 
		ventana1.bsalir.place(x=350, y =200)
		
		# El foco de la aplicación se sitúa en el botón
		# 'self.bcalcular' resaltando su borde. Si se presiona
		# la barra espaciadora el botón que tiene el foco
		# será pulsado. El foco puede cambiar de un widget
		# a otro con la tecla tabulador [tab]
		
		ventana1.bcalcular.focus_set()
		ventana1.mainloop()	

def ventanaVolumen():
		
	ventana1 = Toplevel()
	ventana1.geometry('500x300')
	
	# Impide que los bordes puedan desplazarse para
	# ampliar o reducir el tamaño de la ventana 'self.ventana':
		
	ventana1.resizable(width=True,height=True)
	ventana1.title('Cálculo')
		
		
	# Define el widget Button 'self.bcalcular' que llamará 
	# al metodo 'self.verinfo' cuando sea presionado
	ventana1.lmoles = Label(ventana1, text = "Moles: ").place(x=100, y=60)
	vmoles = IntVar()
	ventana1.emoles = Entry(ventana1, textvariable = vmoles).place(x=250, y=60)

	ventana1.lpresion = Label(ventana1, text = "Presión (atm): ").place(x=100, y=90)
	vpresion = IntVar()
	ventana1.epresion = Entry(ventana1, textvariable = vpresion).place(x=250, y=90)

	ventana1.ltemperatura = Label(ventana1, text = "Temperatura (K): ").place(x=100, y=120)
	vtemperatura = IntVar()
	ventana1.etemperatura = Entry(ventana1, textvariable = vtemperatura).place(x=250, y=120)

	#CALCULA RESULTADO
	#resultado = presion(vvolumen.get(),vmoles.get(),vtemperatura.get())
	ventana1.bcalcular = ttk.Button(ventana1, text='Calcular', 
							command=lambda:imprimir(volumen(vpresion.get(),vmoles.get(),vtemperatura.get()),ventana1))
	
	ventana1.bcalcular.place(x=50, y = 200)

	ventana1.bgraficar = ttk.Button(ventana1, text='Graficar', 
							command=lambda:ventanaIsotermas(volumen(vpresion.get(),vmoles.get(),vtemperatura.get())[1],vmoles.get(),vtemperatura.get()))

	ventana1.bgraficar.place(x=200, y = 200)

	# Coloca el botón 'self.bcalcular' debajo y a la izquierda
	# del widget anterior
	
	ventana1.bsalir = ttk.Button(ventana1, text='Salir', 
							 command=ventana1.destroy)
							 
	# Coloca el botón 'self.bsalir' a la derecha del 
	# objeto anterior.
							 
	ventana1.bsalir.place(x=350, y =200)
		
	# El foco de la aplicación se sitúa en el botón
	# 'self.bcalcular' resaltando su borde. Si se presiona
	# la barra espaciadora el botón que tiene el foco
	# será pulsado. El foco puede cambiar de un widget
	# a otro con la tecla tabulador [tab]
	
	ventana1.bcalcular.focus_set()
	ventana1.mainloop()	

def ventanaMoles():

	ventana1 = Toplevel()
	ventana1.geometry('500x300')
	
	# Impide que los bordes puedan desplazarse para
	# ampliar o reducir el tamaño de la ventana 'self.ventana':
		
	ventana1.resizable(width=True,height=True)
	ventana1.title('Cálculo')
		
		
	# Define el widget Button 'self.bcalcular' que llamará 
	# al metodo 'self.verinfo' cuando sea presionado
	ventana1.lvolumen = Label(ventana1, text = "Volumen (lts): ").place(x=100, y=60)
	vvolumen = IntVar()
	ventana1.evolumen = Entry(ventana1, textvariable = vvolumen).place(x=250, y=60)

	ventana1.lpresion = Label(ventana1, text = "Presión (atm): ").place(x=100, y=90)
	vpresion = IntVar()
	ventana1.epresion = Entry(ventana1, textvariable = vpresion).place(x=250, y=90)

	ventana1.ltemperatura = Label(ventana1, text = "Temperatura (K): ").place(x=100, y=120)
	vtemperatura = IntVar()
	ventana1.etemperatura = Entry(ventana1, textvariable = vtemperatura).place(x=250, y=120)

	#CALCULA RESULTADO
	#resultado = presion(vvolumen.get(),vmoles.get(),vtemperatura.get())
	ventana1.bcalcular = ttk.Button(ventana1, text='Calcular', 
							command=lambda:imprimir(moles(vvolumen.get(),vpresion.get(),vtemperatura.get()),ventana1))
	
	ventana1.bcalcular.place(x=50, y = 200)

	ventana1.bgraficar = ttk.Button(ventana1, text='Graficar', 
							command=lambda:ventanaIsotermas(vvolumen.get(),moles(vvolumen.get(),vpresion.get(),vtemperatura.get())[1],vtemperatura.get()))

	ventana1.bgraficar.place(x=200, y = 200)

	# Coloca el botón 'self.bcalcular' debajo y a la izquierda
	# del widget anterior
	
	ventana1.bsalir = ttk.Button(ventana1, text='Salir', 
							 command=ventana1.destroy)
							 
	# Coloca el botón 'self.bsalir' a la derecha del 
	# objeto anterior.
							 
	ventana1.bsalir.place(x=350, y =200)
		
	# El foco de la aplicación se sitúa en el botón
	# 'self.bcalcular' resaltando su borde. Si se presiona
	# la barra espaciadora el botón que tiene el foco
	# será pulsado. El foco puede cambiar de un widget
	# a otro con la tecla tabulador [tab]
	
	ventana1.bcalcular.focus_set()
	ventana1.mainloop()	

def ventanaTemperatura():

	ventana1 = Toplevel()
	ventana1.geometry('500x300')
	
	# Impide que los bordes puedan desplazarse para
	# ampliar o reducir el tamaño de la ventana 'self.ventana':
		
	ventana1.resizable(width=True,height=True)
	ventana1.title('Cálculo')
		
		
	# Define el widget Button 'self.bcalcular' que llamará 
	# al metodo 'self.verinfo' cuando sea presionado
	ventana1.lvolumen = Label(ventana1, text = "Volumen (lts): ").place(x=100, y=60)
	vvolumen = IntVar()
	ventana1.evolumen = Entry(ventana1, textvariable = vvolumen).place(x=250, y=60)

	ventana1.lpresion = Label(ventana1, text = "Presión (atm): ").place(x=100, y=90)
	vpresion = IntVar()
	ventana1.epresion = Entry(ventana1, textvariable = vpresion).place(x=250, y=90)

	ventana1.lmoles = Label(ventana1, text = "Moles: ").place(x=100, y=120)
	vmoles = IntVar()
	ventana1.emoles = Entry(ventana1, textvariable = vmoles).place(x=250, y=120)

	#CALCULA RESULTADO
	#resultado = presion(vvolumen.get(),vmoles.get(),vtemperatura.get())
	ventana1.bcalcular = ttk.Button(ventana1, text='Calcular', 
							command=lambda:imprimir(temperatura(vvolumen.get(),vmoles.get(),vpresion.get()),ventana1))
	
	ventana1.bcalcular.place(x=50, y = 200)

	ventana1.bgraficar = ttk.Button(ventana1, text='Graficar', 
							command=lambda:ventanaIsotermas(vvolumen.get(),vmoles.get(),temperatura(vvolumen.get(),vmoles.get(),vpresion.get())[1]))

	ventana1.bgraficar.place(x=200, y = 200)

	# Coloca el botón 'self.bcalcular' debajo y a la izquierda
	# del widget anterior
	
	ventana1.bsalir = ttk.Button(ventana1, text='Salir', 
							 command=ventana1.destroy)
							 
	# Coloca el botón 'self.bsalir' a la derecha del 
	# objeto anterior.
							 
	ventana1.bsalir.place(x=350, y =200)
		
	# El foco de la aplicación se sitúa en el botón
	# 'self.bcalcular' resaltando su borde. Si se presiona
	# la barra espaciadora el botón que tiene el foco
	# será pulsado. El foco puede cambiar de un widget
	# a otro con la tecla tabulador [tab]
	
	ventana1.bcalcular.focus_set()
	ventana1.mainloop()	



class Aplicacion():

	def __init__(self):
		self.raiz = Tk()
		self.raiz.geometry('400x500')
		
		self.raiz.resizable(width=True,height=True)
		self.raiz.title('Bienvenido')	

		####################################################################
		self.raiz.boton_gi = ttk.Button(self.raiz, text='Calcular Presion', 
								command=lambda:ventanaPresion()).place(x=50, y=50)
		#self.raiz.boton_gi.grid(row=3,column=2)

		self.raiz.boton_isot = ttk.Button(self.raiz, text='Calcular Volumen', 
								command=lambda: ventanaVolumen()).place(x=50, y=150)
		#self.raiz.boton_isot.grid(row=4,column=2)


		self.raiz.boton_pp = ttk.Button(self.raiz, text='Calcular Moles', 
								command=lambda: ventanaMoles()).place(x=50, y=250)


		self.raiz.boton_pp = ttk.Button(self.raiz, text='Calcular Temperatura', 
								command=lambda: ventanaTemperatura()).place(x=50, y=350)
		#self.raiz.boton_pp.grid(row=6,column=2)

		####################################################################
			# Mostrar la ventana
		self.raiz.mainloop()		


def main():
	mi_app = Aplicacion()
	return 0

main()
