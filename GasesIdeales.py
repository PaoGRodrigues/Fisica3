## Constantes
const_gases = (0.08206,"atm * L / (mol * K)")
num_Avogadro = 6.022e23

########
### Ecuacion de los gases ideales
########
def gases_ideales(presion, volumen, moles, temperatura):

	resultado = []
	operandos = {'Presion': presion, 'Volumen': volumen, 'Moles': moles, 'Temperatura': temperatura}

	oper_values = (list(operandos.values()))
	if(oper_values.count(0) <=2):
		
		##### PV = nRT
		if(presion==0):
			resultado = ["Presion", round((operandos['Moles']*const_gases[0]*operandos['Temperatura'])/operandos['Volumen'], 3), "atm"]
		elif(volumen==0):
			resultado = ["Volúmen", round((operandos['Moles']*const_gases[0]*operandos['Temperatura'])/operandos['Presion'], 3), "litros"]
		elif(moles==0):
			resultado = ["Moles", round((operandos['Presion']*operandos['Volumen'])/(const_gases[0]*operandos['Temperatura']), 3), "moles"]
		else:
			resultado = ["Temperatura", round((operandos['Presion']*operandos['Volumen'])/(const_gases[0]*operandos['Moles']), 3), "kelvin"]
	else:
		resultado = '-1'

	return resultado

########
### Crear diccionario.
########
def crear_dic(listaKeys, listaValues):
	
	return(dic(zip(listaKeys,listaValues)))

def values_null(Dic, func):
	oper_values = list(Dic.values())


def cantidad_fija(p1, p2, v1, v2, t1, t2):

	crear_dic(['Presion1','Presion2','Volumen1','Volumen2','Temperatura1','Temperatura2'], [p1,p2,v1,v2,t1,t2])
