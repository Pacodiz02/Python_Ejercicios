#Ejercicio4
lista=[]

num = int(input("Dígame cuántas palabras tiene la lista: "))
while num<=0:
    print("Error, vuelva a intentarlo.")
    num = int(input("Dígame cuántas palabras tiene la lista: "))
contador = 0

for i in range (0, num):
    contador += 1
    cad = input("Dime la palabra %i: "% (contador))
    lista.append(cad)
print("La lista creada es: ", lista)

print("\n")
print("Opciones:")
print("1. Contar")
print("2. Modificar")
print("3. Eliminar")
print("0. Salir")

opcion = input("Elige opción: ")
while opcion != "0":
    contador1 = 0
    if opcion == "1":
        buscar = input("Dígame la palabra a buscar: ")
        for a in lista:
            if buscar == a:
                contador1 += 1
        print("La palabra %s aparece %i veces en la lista" %(buscar,contador1))
    
    if opcion == "2":
        palabra = input("Sustituir la palabra: ")
        sustituto = input("Por la palabra: ")
        for a in lista:
            if palabra in lista:
                lista.insert(1,sustituto)
                lista.remove(palabra)
        print("La lista es ahora: ", lista)
    
    if opcion == "3":
        eliminar = input("Palabra a eliminar: ")
        for a in lista:
            if eliminar in lista:
                lista.remove(eliminar)
        print("La lista es ahora: ", lista)

    print("\n")
    print("1. Contar")
    print("2. Modificar")
    print("3. Eliminar")
    print("0. Salir")
    opcion = input("Elige opción: ")

print("Adioss!!")