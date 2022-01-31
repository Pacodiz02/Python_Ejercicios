#Ejercicio3

alumnos=[]
notas=[]
todnotas=[]
medias=[]

cuantosalum=int(input("¿Cuántos alumnos tiene la clase? "))

while cuantosalum<1:
    print("VALOR INCORRECTO, introduzca el número de alumnos de nuevo.")
    cuantosalum=int(input("¿Cuántos alumnos tiene la clase? "))

for a in range(0,cuantosalum):

    nombrealum=input("Nombre del alumno: ")
    alumnos.append(nombrealum)

    cuantasnotas=int(input("¿Cuántas notas tiene el alumno? "))
    
    acum=0

    notas=[]

    for i in range(0,cuantasnotas):
        
        nota=int(input("Nota: "))
        while nota <1 and nota >10:
            print("VALOR INCORRECTO, introduzca una nota valida(1-10).")
            nota=int(input("Nota: "))
        notas.append(nota)
        
        acum+=nota

    media=acum / cuantasnotas
    medias.append(media)
    
    todnotas.append(notas)

print("\n")

print("1. Nota media")
print("2. Buscar por nombre")
print("3. Añadir alumno")
print("4. Eliminar alumno")
print("5. Salir")

opcion=input("Introduce una opción: ")

while opcion!="5":

    if opcion == "1":
        for a in medias:
            posicion=medias.index(a)
            if a >= 5:
                print("El alumno %s está aprobado." %(alumnos[posicion]))
            else:
                print("El alumno %s está suspenso." %(alumnos[posicion]))

    checknombre=False    
    if opcion == "2":
        nombre1=input("Dime un nombre a buscar: ")
        for a in alumnos:
            if nombre1 == a:
                checknombre=True
                posicion=alumnos.index(a)
                print("El alumno %s tiene las notas: %s" %(a,todnotas[posicion]))   
        if checknombre==False:
            print("Alumno no encontrado")
            

    if opcion == "3":
        nombrealum=input("Nombre del nuevo alumno: ")
        alumnos.append(nombrealum)

        cuantasnotas=int(input("¿Cuántas notas tiene el alumno? "))

        acum=0

        notas=[]

        for i in range(0,cuantasnotas):

            nota=int(input("Nota: "))
            while nota <1 and nota >10:
                print("VALOR INCORRECTO, introduzca una nota valida(1-10).")
                nota=int(input("Nota: "))
            notas.append(nota)

            acum+=nota

        media=acum / cuantasnotas
        medias.append(media)

        todnotas.append(notas)

        print("Lista de alumnos actulizada: " ,alumnos)


    if opcion == "4":
        alumeliminar=input("Nombre del alumno que desea eliminiar: ")
        for a in alumnos:
            if a == alumeliminar:
                posicion=alumnos.index(a)
                alumnos.remove(a)
                todnotas.pop(posicion)
        print("Lista de alumnos actualizada: ",alumnos)        

    print("\n")

    print("1. Nota media")
    print("2. Buscar por nombre")
    print("3. Añadir alumno")
    print("4. Eliminar alumno")
    print("5. Salir")

    opcion=input("Introduce una opción: ")