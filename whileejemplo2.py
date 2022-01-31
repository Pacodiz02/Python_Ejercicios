#un programa que lea dos numeros y que el primero sea mas pequeño que el segundo y
# si no es asi de un error
#si si ocurre pedir un numero y decir si esta dentro del intervalo o no

num1=float(input("Introduce un número: "))
num2=float(input("Introduce otro número: "))
while num1<num2:
    print("ERROR")
    num1=float(input("Introduce un número: "))
    num2=float(input("Introduce otro número: "))
num3=float(input("Introduce un tercer número: "))

if num3 < num1 or num2 >num3:
    print("El número está dentro del intervalo de los números introducidos")
else:
    print("El número no está dentro del intervalo de los números introducidos") 