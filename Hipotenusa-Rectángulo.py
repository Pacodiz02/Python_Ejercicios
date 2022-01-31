#Calcular la hipotenusa de un rectágulo a partir de catetos
import math
cat1=float(input("Introduce el CATETO 1: "))
cat2=float(input("Introduce el CATETO 2: "))
res=math.sqrt(cat1**2 + cat2**2)
print("El resultado es: ", res)