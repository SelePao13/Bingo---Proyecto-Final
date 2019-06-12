#Juego BINGO
Nombre_de_Jugador=[]
Cartillas=[]
print("""
     ________    _______________
    |   ___  \\  /              /
    |  |   \\  |/              /\\
    |  |   |  |__  ___     __/ _\\____   ______
    |  |__/  /|  |/   \\   |  |/  ____\\ /  __  \\
    |   __  < |  |     \\  |  |  |     |  |  |  |
    |  |  \\  \\|  |  |\\  \\ |  |  |  ___|  |  |  |
    |  |   |  |  |  | \\  \\|  |  | /_  |  |  |  |
    |  |___/  |  |  |  \\     |  |__/  |  |__|  |
    |________/|__|\\_|  /\\___/ \\______/\\\\______/
      /               /\\               \\
     /______JUEGO_____/DE\\____NUMEROS____\\
""")

jugadores = int(input("Digite numero de jugadores: "))
while True:
        a = input("Nombre de jugador:")
        Nombre_de_Jugador.append(a)
        while True:
            b = int(input("Numero de cartillas:"))
            if b <= 3:
                Cartillas.append(b)
                break
        if len(Nombre_de_Jugador) == jugadores:
            break
suma = 0 
for x in Cartillas:
    suma = suma + x

Pozo_Total = suma*5

def pedirNumeroEntero():

	correcto=False
	num=0
	while(not correcto):
		try:
			num = int(input("Introduce opcion: "))
			correcto=True
		except ValueError:
			print('Error, introduce opcion')
	
	return num

salir = False
opcion = 0
cad=""
while not salir:

	print ("1. Jugar")
	print ("2. Resultado")
	print ("3. Reiniciar juego")
	print ("4. Finalizar juego")
	
	print ("Elige una opcion")

	opcion = pedirNumeroEntero()
	

	if opcion == 1:
		import random
		for x in range(1):
			a=random.randint(1,80)
			print("Su bolilla es", a)
			cad = cad + " " + str(a)
			
	elif opcion == 2:
		import random  
		bolillas=[random.randint(1, 80)]
		i=1
		while i<15:
			x=random.randint(1,80)
			for j in range(0, len(bolillas)):
				if bolillas[j]==x:
					break
			else:
				bolillas.append(x)
				i+=1
				print("Las bolillas son:",cad)
				break
	elif opcion == 3:
		print("Reiniciar juego")
	elif opcion == 4:
		print("El pozo total es: S/",Pozo_Total)
		salir = True
	else:
		print ("Introduce un opcion 1 y 3")

print ("Fin")
