#Ejercicio 2

cad=input("Introduce una cadena de caracteres: ")
caracter=input("Introduce un caracter: ")
posiblescaracteres="abcdefghijkmnlñopqrstuvwxyzABCDEFGHIJKMNLÑOPQRSTUVWXYZ1234567890"

while caracter not in posiblescaracteres:
    print("ERROR")
    cad=input("Introduce una cadena de caracteres: ")
    caracter=input("Introduce un caracter: ")

if caracter in cad:
    print("Está el caracter en la cadena. ")

else:
    print("No esta en la cadena")