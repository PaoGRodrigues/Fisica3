##### @param U: energía interna
##### @param Q: calor
##### @param W: trabajo

def formula(U, Q, W):
	resultado = []
	operandos = {'U': U, 'Q': Q, 'W': W}

	oper_values = (list(operandos.values()))
	if(oper_values.count(0) <=2):
		
		##### PV = nRT
		if(U==0):
			resultado = ["Energía Interna", round(operandos['Q']+operandos['W'], 3), "J"]
		elif(Q==0):
			resultado = ["Calor", round(operandos['U']-operandos['W'], 3), "calorías"]
		else:
			resultado = ["Trabajo", round(operandos['U']-operandos['Q'], 3), "J"]
	else:
		resultado = '-1'

	return resultado
