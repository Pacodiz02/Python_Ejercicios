#Ejercicio 4

cad1=input("Introduce una cadena de caracteres: ")

while len(cad1)<1:
    print("La cadena  de caracteres debe tener 1 carácter como mínimo.")
    cad1=input("Introduce una cadena de caracteres: ")

cad2=input("Introduce otra cadena de caracteres: ")

while len(cad1)<1:
    print("La cadena  de caracteres debe tener 1 carácter como mínimo.")
    cad2=input("Introduce otra cadena de caracteres: ")

cad1g=cad1.lower()
cad2g=cad2.lower()

if cad1g.find(cad2g) > -1:
    print("La segunda cadena es una subcadena de la primera.")

else:
    print("La segunda cadena no es una subcadena de la primera")