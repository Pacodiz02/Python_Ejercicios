alumnos=[]

nombre=input("Alumno: ")
while nombre!="*":
    alumno=[]
    edad=int(input("Edad: "))
    alumno.append(nombre)
    alumno.append(edad)
    alumnos.append(alumno)
    nombre=input("Alumno: ")

edad_max=0

for alum in alumnos:
    if alum[1]>=18 :
        print("Es mayor de 18" ,alum[0])

    
    if alum[1] > edad_max:
        edad_max=alum[1]

for alum in alumnos:
    if alum[1] == edad_max:
        print("La edad de los mas mayores: ", alum[0])

#print(alum[0],alum[1])

