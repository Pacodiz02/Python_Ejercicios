#Ejercicio 1

num1=int(input("Introduce un número entero: "))
num2=int(input("Introduce un número entero mayor que el anterior: "))
acom=0

while num2<num1:
    print("¡¡El segundo número entero tiene que ser mayor que el primero!! ")
    num1=int(input("Introduce un número entero: "))
    num2=int(input("Introduce un número entero mayor que el anterior: "))
if num1<num2:
    for i in range(num1,num2+1):
        acom=i+acom
    print("La suma de los numeros enteros que hay entre los introducidos es: ",acom)
