#leemos la cadena 1 y leemos la cadena 2 y q compruebe q la cadena 2 es una subcadena de la 1

cad1=input("Introduce una cadena de caracteres: ")
cad2=input("Introduce otra cadena: ")

if cad2 in cad1:
    print("La subcadena esta dentro de la cadena")
else:
    print("La subcadena no esta dentro de la cadena")