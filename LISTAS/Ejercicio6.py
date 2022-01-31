#Ejercicio 6

dias=[31,28,31,30,31,30,31,31,30,31,30,31]
meses=["enero","febrero","marzo", "abril", "mayo","junio", "julio", "agosto", "septiembre","octubre","noviembre","diciembre"]

mes=int(input("Dime el número de un mes: "))
while mes<1 or mes>12:
    print("ERROR, MES INCORRECTO")
    mes=int(input("Dime el número de un mes: "))

print("El mes %s tiene %d días" %(meses[mes-1],dias[mes-1]))

#print("El mes %s tiene %d días" %(meses[mes-1][0],dias[mes-1][1]))