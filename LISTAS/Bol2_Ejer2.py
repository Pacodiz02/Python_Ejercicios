lista1=[]
lista2=[]

num_palabras=int(input("Palabras en primera lista: "))
num_palabras2=int(input("Palabras en segunda lista: "))

for i in range (0, num_palabras):
    palabra=input("Introduce un palabra: ")
    lista1.append(palabra)
for i in range (0, num_palabras2):
    palabra2=input("Introduce un palabra: ")
    lista1.append(palabra2)

for i in lista2:
    while i in lista1:
        lista1.remove(i)
    for cont in range(lista1.count(1)):
        lista1.remove(i)
        

 