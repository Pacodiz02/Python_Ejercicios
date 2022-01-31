#Ejercicio 2
print("¡Introduce números hasta acertar el número secreto!")

num=int(input("Introduce un número entero positivo:  "))
count=0
mayor=0
menor=num
totaln=num
Anterior=num

while num !=0:
    if num<0:
        print("¡El número tiene que ser positivo!")
    count=count+1
    if num>mayor:
        mayor=num
    if num<menor:
        menor=num
    totaln=totaln+num
    num=int(input("Introduce un número entero positivo:  "))

if num==0:
    print("¡¡Has acertado el número secreto para salir del bucle!!")

media=totaln/count
print("Has introducido %i numeros. "%(count))
print("El número menor introducido es: ",menor)
print("El número mayor introducido es: ",mayor)
print("La media de los números intrducidos es: ",media)