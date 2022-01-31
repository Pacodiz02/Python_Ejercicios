#Ejercicio 1

lista=[]
check=False

rango=int(input("Introduce el número de cadenas que se van a introducir: "))
while rango <=0:
    print("ERROR, vuelva a intentarlo.")
    rango=int(input("Introduce el número de cadenas que se van a introducir: "))

for i in range (0, rango):
    cadenas=(input("Introduce la cadena: "))
    lista.append(cadenas)

cadena2=(input("Introduce una segunda cadena: "))
for var in lista:
    if cadena2 in lista:
        check=True
        lista.remove(cadena2)
if check==True:
    print("La lista sería: ",lista)

else:
    print("La segunda cadena introducida no se encuentra en la lista.")