#pide cadena y subcadena y dice en que posicion esta la subcadena dentro de la cadena
cad1=input("Introduce una cadena de caracteres: ")
cad2=input("Introduce otra cadena: ")
pos=0

if cad2 in cad1:
    print("La subcadena esta dentro de la cadena")
    print("La subcadena aparece: ")
    print(cad1.count(cad2))
else:
    print("La subcadena no esta dentro de la cadena")

print("La subcadena se encuentra en la posición:")
for i in range(0, cad1.count(cad2)):
    print(cad1.find(cad2 ,pos+1))
    pos=cad1.find(cad2 ,pos)+1

