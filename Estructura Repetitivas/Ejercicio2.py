import random
cont=0
num=int(input("Introduce un número entre el 1 y el 100: "))

randomnum= random.randint(1,100)

intentos=10

while num != randomnum and intentos>1:
    if num < randomnum:
        print("El número que buscas es mayor")
    else:
        print("El número que buscas es menor")

    intentos=intentos-1
    print("Te quedan %i" %(intentos))

    num=int(input("Introduce un número entre el 1 y el 100: "))

if num == randomnum:
    print("¡¡¡Ese es el número!!!")