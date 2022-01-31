#Ejercicio 5
#Los usuarios son: usuario, manolo, carmelo y juan. Las contraseñas son usuario, hola, hola y hola, respectivamente.

from crypt import crypt

#No me funciona con la ruta relativa y he tenido que poner la ruta absoluta para probarla, pero me dijo jose domingo que pusiera la relativa de todos modos.
f=open("passwd.txt")
lineas=f.readlines()
f.close()

lista=[]

for linea in lineas:
    lista.append(linea.split(":"))

nombre=input("Nombre: ")
check=False
check1=False
for usuario in lista:
    if nombre==usuario[0]:
        check=True
        sal=(usuario[1][:30])
        passwd=input("Contraseña: ")
        valor=crypt(passwd,sal)
        if usuario[1] == valor:
            check1=True
            print("\n")
            print("ACCESO PERMITIDO")
if check1 == False:
    print("ACCESO DENEGADO")
if not check:
    print("Usuario no existe")