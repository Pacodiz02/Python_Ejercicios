lista=[]

num=int(input("Introduce un número: "))
while num!=0:
    lista.append(num)
    num=int(input("Introduce un número: "))

for num in lista:
    print(num,end=" ")
print()

# OTRA FORMA PARA PRINTEAR SOLO SI ES STR
# print "" join.lista

print(len(lista))
print(sum(lista))
print(max(lista))
print(min(lista))

#Mostrar elementos lista ordenados.

for num in sorted(lista):
    print(num,end=" ")
print()
print("Hemos terminado")