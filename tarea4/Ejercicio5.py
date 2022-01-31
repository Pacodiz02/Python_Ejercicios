#Ejercicio 5

cad=input("Introduce una cadena de caracteres: ")

while len(cad)<1:
    print("¡TIENES QUE INTRODUCIR UNA CADENA!")
    cad=input("Introduce una cadena de caracteres: ")

caracterepe=False

for c in cad:
    if cad.count(c)>1:
        caracterepe=True

if caracterepe:
    print("La cadena tiene caracteres repetidos.")

else:
    print("La cadena no tiene caracteres repetidos.")