#Ejercicio 1

año1=int(input("¿En que año estamos? "))
año2=int(input("Introduce un año cualquiera: "))

while año1<0 or año2<0:
    print("No existen los años introducidos")
    año1=int(input("¿En que año estamos? "))
    año2=int(input("Introduce un año cualquiera: "))

if año2>año1:
    resta1=año2-año1

    if resta1==1:
        print("Para llegar al año %i falta solo %i año." %(año2,resta1))
    else:print("Para llegar al año %i faltan %i años." %(año2,resta1))

if año1>año2:
    resta2=año1-año2
    
    if resta2==1:
        print("Desde el año %i ha pasado solo %i año."%(año1,resta2))
    
    else:
        print("Desde el año %i han pasado %i años."%(año1,resta2))

if año1==año2:
    print("¡Son el mismo año!")
