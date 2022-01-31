# cuantos elementos va a tener una lista numeros y los guarde en la lista. ahora el programa dice si esta o no en la lista.
lista=[]
cantidad=int(input("¿Cuántos números vas a introducir? "))
for i in range(0, cantidad):
    num=int(input("Número: "))
    lista.append(num)

otronum=int(input("Otro número: "))

if otronum in lista:
    print("Está en la lista")

else:
    print("No está en la lista")

for par in sorted(lista):
    if par%2==0:
        print(par,end=" ")
    print()