def ComprobarNumeroPositivo(numero):
    if numero >=0:
        return True
    return False

#Programa principal
import math

num=int(input("Introduce un número: "))

if ComprobarNumeroPositivo(num):
    print("El número es positivo")

else:
    print("El número es negativo")

