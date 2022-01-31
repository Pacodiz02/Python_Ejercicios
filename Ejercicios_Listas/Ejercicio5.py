#Ejercicio 5

lista = []

print("1. Añadir número a la lista")
print("2. Añadir número de la lista en una posición")
print("3. Longitud de la lista")
print("4. Eliminar el último número")
print("5. Eliminar un número")
print("6. Contar números")
print("7. Posiciones de un número")
print("8. Mostrar números")
print("9. Salir")

opcion = input("Elige una opción: ")

while opcion != "9":

    if opcion == "1":
        num1 = int(input("¿Qué número desea añadir? "))
        lista.append(num1)
    
    if opcion == "2":
        num2 = int(input("¿Qué número desea añadir? "))
        posicion = int(input("¿En qué posición desea añadirlo? "))

        while posicion < 1:
            print("¡Valor incorrecto! El valor de la posición debe ser mayor que 1.")

            posicion = int(input("¿En qué posición desea añadirlo? "))

        lista.insert(posicion,num2)
    
    if opcion == "3":
        print("Longitud de la lista ahora es de: ", len(lista))
    
    if opcion == "4":
        print("El último número de la lista es: ", lista[-1])
        lista.pop()
        print("Así queda la lista borrando el último número: ", lista)
    
    if opcion == "5":
        posicion2 = int(input("Introduzca una posición: "))

        while posicion2 < 1:
            print("¡Valor incorrecto! El valor de la posición debe ser mayor que 1.")
            
            posicion2 = int(input("Introduzca una posición: "))
        
        lista.remove(lista[posicion2])
    
    if opcion == "6":
        num6 = int(input("Introduzca el número que desea buscar: "))
        print("El número introducido aparece en la lista, %i veces." %(lista.count(num6)))
    
    if opcion == "7":
        num7 = int(input("¿Qué número desea buscar? "))
       
        while num7 < 1:
            print("¡Valor incorrecto! El valor no debe de ser menor que 1.")

            num7 = int(input("¿Qué número desea buscar? "))
            
        print("La posición en la que se encuentra es: ", lista.index(num7))
    
    if opcion == "8":
        print("Los números de la lista son: ", lista)

    print("\n")
    print("1. Añadir número a la lista")
    print("2. Añadir número de la lista en una posición")
    print("3. Longitud de la lista")
    print("4. Eliminar el último número")
    print("5. Eliminar un número")
    print("6. Contar números")
    print("7. Posiciones de un número")
    print("8. Mostrar números")
    print("9. Salir")
    opcion = input("Elige una opción: ")