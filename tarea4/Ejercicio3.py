#Ejercicio 3

dni=input("Introduzca su DNI: ")

while len(dni)!=9:
    print("El DNI introducido debe tener 9 caracteres.")
    dni=input("Introduzca de nuevo su DNI: ")

letra=dni[8]

numeros=int(dni[:8])

cod="TRWAGMYFPDXBNJZSQVHLCKE"

calc=cod[numeros%23]

if letra.upper()==calc:
    print("El DNI introducido es válido.")

else:
    print("El DNI introducido no es válido.")