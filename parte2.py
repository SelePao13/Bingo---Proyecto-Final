import time
def timer(z):
        while z!=0:
            z=z-1
            time.sleep(z)#time.sleep(seconds) #here you can mention seconds according to your requirement.

# Pidiendo el nombre de usuario
while True:
    n = int(input("¿Cuántos jugarán?: "))
    j=[]
    N=[]
    for i in range (n):
        nombre=input("Nombre de jugador: ")
        cartilla=int(input("¿Cuántas cartillas escogerá?: "))
        N.append(cartilla)
        m=[]
        m.append(nombre)
        m.append(cartilla)
        j.append(m)
    print(j)
    
    suma=0
    for i in N:
        suma = suma + i

    suma2 = 0
    suma2 = suma*5
    print("El pozo es: ",suma2)
    

    print("El juego ha empezado")


    import random
    B=[]
    for i in range(1,81):
        B.append(i)

    while True:
        for i in range(15):
            C=random.choice(B)
            B.remove(C)

            #D=[]
            #D.append(C)
            print("Bolilla n° ",C)     
            
            timer(4)
    
        m=input("¿Deseas continuar?: ")
        if m=="no":
            break
     
    reinicio=input("¿Desea reiniciar el juego?: ")
    if reinicio=="no":
        
        print("El juego ha finalizado")
        
        break