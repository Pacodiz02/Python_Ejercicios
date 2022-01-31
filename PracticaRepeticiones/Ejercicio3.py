#Ejercicio 
usuario=input("Usuario: ")
passwd=input("Contraseña: ")

intentos=3

for i in range(1,intentos):
    if usuario=="root" and passwd=="1234":
        print(" ¡Bienvenido al sistema! ")
        break;
    if usuario!="root" or passwd!="1234":

        print("Intentelo de nuevo, le quedan %s intentos"%(3-i))
        usuario=input("Usuario: ")
        passwd=input("Contraseña: ")
        var=i
if var==2:
    print("Se ha superado el máximo número de intentos")