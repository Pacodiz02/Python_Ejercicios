#Crear una lista q pida 5 cadenas y 
#que copie la lista en otra en inverso y la muestre

lista1=[]
lista2=[]

for i in range(0,5):
    cad=input("Introduce una cadena: ")
    lista1.append(cad)

lista2=lista1[::-1]
for var in lista2:
    print(var,end=" ")
print()

print(", ".join(lista2))
