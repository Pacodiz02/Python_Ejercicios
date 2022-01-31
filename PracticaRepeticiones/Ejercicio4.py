#Ejercicio 4

num=int(input("Introduce un número: "))

cont=0
suma=0

while cont<10 or suma<=100:
    
    suma=suma+num
    cont=cont+1

    if cont==10:
        print("Se han introducido 10 números.")
        
        break;

    if  suma>100:
        print("La suma de los números introducidos es superior a 100.")

        break;

    print("¡Sigue introduciendo números!")
    num=int(input("Introduce un número: "))
