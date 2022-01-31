#Ejercicio 4

equipos=[]
resultados=[]

for a in range(0,14):
    
    equipo1=input("Introduce el equipo local: ")
    equipo2=input("Introduce el equipo visitante: ")

    equipos.append([equipo1,equipo2])

    resultado1=int(input("Introduce el resultado del equipo local: "))
    resultado2=int(input("Introduce el resultado del equipo visitante: "))

    resultados.append([resultado1,resultado2])

    print("\n")

print("La quiniela de la jornada es: \n")

for a in equipos:
    posicion=equipos.index(a)
    print("Equipos:",equipos[posicion], "- Resultado: " ,resultados[posicion])