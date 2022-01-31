import math
sueldo=float(input("Introduce sueldo base: "))
primera=float(input("Introduce primera venta: "))
segundo=float(input("Introduce segunda venta: "))
tercera=float(input("Introduce tercera venta: "))
comision=primera*0.1+segundo*0.1+tercera*0.1
sueldototal= comision + sueldo
print("La comisión es " ,comision)
print("La comisión es " ,sueldototal)
