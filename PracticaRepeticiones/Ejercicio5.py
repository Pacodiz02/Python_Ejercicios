#Ejercicio 5

num=int(input("Introduce la cantidad vendida: "))
precio=float(input("Introduce el precio de la unidad: "))

total=num*precio

while num<0 or precio<0:
    print("¡¡La cantidad vendida o el precio introducido no puede ser menor que 0!!")
    
    num=int(input("Introduce la cantidad vendida: "))
    precio=float(input("Introduce el precio de la unidad: ")) 

if num>0 and precio>0:
    print("El importe total es: ",total)
  