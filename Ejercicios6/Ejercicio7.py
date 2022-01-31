#Ejercicio 7

centimos=[50000,20000,10000,5000,2000,1000,500,200,100,50,20,10,5,2,1]

cantitotal=float(input("Cantidad total: "))
cantientregada=float(input("Cantidad entregada: "))

cantidevolver=(cantientregada-cantitotal)
cantidevolver2=round((cantientregada-cantitotal)*100)

print("Cantidad a devolver:", cantidevolver, "€")

print("\n")

if cantidevolver2/centimos[0]>=1:
	print("%d Billete de 500 euros" % (cantidevolver2/centimos[0]))
	cantidevolver2=cantidevolver2%centimos[0]

if cantidevolver2/centimos[1]>=1:
	print("%d Billete de 200 euros" % (cantidevolver2/centimos[1]))
	cantidevolver2=cantidevolver2%centimos[1]

if cantidevolver2/centimos[2]>=1:
	print("%d Billete de 100 euros" % (cantidevolver2/centimos[2]))
	cantidevolver2=cantidevolver2%centimos[2]

if cantidevolver2/centimos[3]>=1:
	print("%d Billete de 50 euros" % (cantidevolver2/centimos[3]))
	cantidevolver2=cantidevolver2%centimos[3]

if cantidevolver2/centimos[4]>=1:
	print("%d Billete de 20 euros" % (cantidevolver2/centimos[4]))
	cantidevolver2=cantidevolver2%centimos[4]

if cantidevolver2/centimos[5]>=1:
	print("%d Billete de 10 euros" % (cantidevolver2/centimos[5]))
	cantidevolver2=cantidevolver2%centimos[5]

if cantidevolver2/centimos[6]>=1:
	print("%d Billete de 5 euros" % (cantidevolver2/centimos[6]))
	cantidevolver2=cantidevolver2%centimos[6]

if cantidevolver2/centimos[7]>=1:
	print("%d moneda de 2 euros" % (cantidevolver2/centimos[7]))
	cantidevolver2=cantidevolver2%centimos[7]

if cantidevolver2/centimos[8]>=1:
	print("%d moneda de 1 euro" % (cantidevolver2/centimos[8]))
	cantidevolver2=cantidevolver2%centimos[8]

if cantidevolver2/centimos[9]>=1:
	print("%d moneda de 50 centimos" % (cantidevolver2/centimos[9]))
	cantidevolver2=cantidevolver2%centimos[9]

if cantidevolver2/centimos[10]>=1:
	print("%d moneda de 20 centimos" % (cantidevolver2/centimos[10]))
	cantidevolver2=cantidevolver2%centimos[10]

if cantidevolver2/centimos[11]>=1:
	print("%d moneda de 10 centimos" % (cantidevolver2/centimos[11]))
	cantidevolver2=cantidevolver2%centimos[11]

if cantidevolver2/centimos[12]>=1:
	print("%d moneda de 5 centimos" % (cantidevolver2/centimos[12]))
	cantidevolver2=cantidevolver2%centimos[12]

if cantidevolver2/centimos[13]>=1:
	print("%d moneda de 2 centimos" % (cantidevolver2/centimos[13]))
	cantidevolver2=cantidevolver2%centimos[13]

if cantidevolver2/centimos[14]>=1:
	print("%d moneda de 1 centimo" % (cantidevolver2/centimos[14]))
	cantidevolver2=cantidevolver2%centimos[14]



