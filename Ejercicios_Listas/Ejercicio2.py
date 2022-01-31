from random import randint

lista=[]

for i in range (0,10):
    aleatorio= randint(0,100)
    lista.append(aleatorio)
print(lista)
print("\n")

suma=0
media=0
contador=0

for i in lista:
    contador += 1
    suma= suma+i
    media= suma / contador

print("1. Sumar")
print("2. Máximo")
print("3. Media")
print("4. Salir")

veces=input("Opción: ")
while veces!="4":
    if veces == "1":
        print("La suma es: ", suma)
    if veces == "2":
        print("El número máximo de la lista es: ", max(lista))
    if veces == "3":
        print("La media es: ", media)
    
    print("1. Sumar")
    print("2. Máximo")
    print("3. Media")
    print("4. Salir")
    veces=input("Opción: ")
