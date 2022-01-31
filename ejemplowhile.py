#un programa que me pida un umeruo mientras el numero sea negativo de error y vuelva a pedir, numero positivo muestra cuadrado del numero
num=float(input("Introduce un número: "))
while num <0:
    print("El número es negativo INCORRECTO")
    num=float(input("Introduce un número"))
print("El número es positivo, CORRECTO",num**2)
print("Fin del programa")
