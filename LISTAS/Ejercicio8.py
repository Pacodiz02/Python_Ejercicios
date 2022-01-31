#Ejercicio 8

nombres=[]
edades=[]

nombre=input("Introduce un nombre: ")

while nombre!="*":
    edad=int(input("Introduce la edad: "))
    nombres.append(nombre)
    edades.append(edad)
    nombre=input("Introduce un nombre: ")

# Mostramos alumnos mayores de edad
for alum,edad in zip(nombres,edades):
    if edad>=18:
        print(alum)

# Mostramos los alumnos de mayor edad
edad_max=max(edades)
for alum,edad in zip(nombres,edades):
    if edad==edad_max:
        print(alum)