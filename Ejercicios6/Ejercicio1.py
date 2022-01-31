#Ejercicio 1

articulos=[]
precios=[]
mas100=[]

numArti=int(input("Introduce el número de articulos a introducir: "))

while numArti<1:
    print("Error, se deben introducir como mínimo 1 artículo.")
    numArti=int(input("Introduce el número de articulos a introducir: "))

cont=0
acom=0

for i in range (0,numArti):
    
    cont+=1
    articulo=input("Introduce el artículo: ")
    articulos.append(articulo)
    
    precio=float(input("Introduce el precio del artículo introducido: "))
    precios.append(precio)
    acom+=precio

    media= acom / cont

    if precio >100:
        mas100.append(articulo)

artibuscar=input("Introduce el nombre del artículo a buscar: ")

check=False

for a in articulos:
    if artibuscar == a:
        check= True
        posicion= articulos.index(a)
        print("El articulo existe")
        print("El precio del articulo %s es %s: " %(a ,precios[posicion]))

if check == False:
    print("El articulo no existe")

print("La media de los precios es: ",media)
print("Los articulos que cuestan más de 100€ son: ",mas100)