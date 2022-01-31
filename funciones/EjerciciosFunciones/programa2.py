#Ejercicio 2

from funciones_fecha import LeerFecha,CalcularDiaJuliano

d1,m1,a1=LeerFecha()
d2,m2,a2=LeerFecha()

dj1=CalcularDiaJuliano(d1,m1,a1)
dj2=CalcularDiaJuliano(d2,m2,a2)

print(abs(dj1-dj2))

 