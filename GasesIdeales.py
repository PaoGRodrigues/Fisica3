## Constantes
const_gases = (0.08206,"atm * L / (mol * K)")
num_Avogadro = 6.022e23

########
### Ecuacion de los gases ideales
########
def presion(volumen, moles, temperatura):
	if(temperatura>=0 and volumen != 0):
		resultado = ["Presion", round((moles*const_gases[0]*temperatura)/volumen, 3), "atm"]

	return resultado

def moles(volumen, presion, temperatura):
	if(temperatura!= 0):
		resultado = ["Moles", round((presion*volumen)/(const_gases[0]*temperatura), 3), "moles"]
	
	return resultado

def volumen(presion, moles, temperatura):
	if(temperatura>=0 and presion != 0):
		resultado = ["Volúmen", round((moles*const_gases[0]*temperatura)/presion, 3), "litros"]
	
	return resultado

def temperatura(volumen, moles, presion):
	if(moles != 0):
		resultado = ["Temperatura", round((presion*volumen)/(const_gases[0]*moles), 3), "kelvin"]
	
	return resultado