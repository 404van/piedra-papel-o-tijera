import random



def ingresar_jugada():
	print("1-Piedra")
	print("2-Papel")
	print("3-tijera")
	jugada = int(input("Ingrese jugada: "))
	return(jugada)

def jugada_ia():
	jugada = random.randint(1, 3)
	return(jugada)


def mostrar_mano(eleccion, identidad):
	if eleccion == 1:
		eleccion = "Piedra"	
	if eleccion == 2:
		eleccion = "Papel"	
	if eleccion == 3:
		eleccion = "Tijera"	
	#print(eleccion)
	print("{} elejió {}".format(identidad, eleccion))

def ganador(jugador, maquina):

	if jugador+1==maquina or jugador==maquina+2 :
		print("gana inteligencia artificial")
	elif maquina+1==jugador or maquina==jugador+2 :
		print("gana usuario")
	else:print("empate")


def main():
	jugador = ingresar_jugada()
	maquina = jugada_ia()
	mostrar_mano(maquina, "inteligencia artificial")
	mostrar_mano(jugador, "usuario")
	ganador(jugador, maquina)



main()