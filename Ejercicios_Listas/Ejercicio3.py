temperaturas='''Utrera,29,12
Dos Hermanas,32,14
Sevilla,30,15
Alcalá de Guadaíra,31,14'''

lista=temperaturas.splitlines()
lista2=[]
for i in lista:
    datos=i.split(",")
    lista2.append(datos)

media=0

for a in lista2:
    media= (int(a[1]) + int(a[2])) / 2
    print(a[0],media)

check=False
print("\n")

poblacion=input("Introduce la población: ")
for o in lista2:
    
    if poblacion==o[0]:
        check=True

        if check:
            print("Temperatura máxima: ", o[1], "\n" "Temperatura mínima: ", o[2])

if check==False:
    print("Error, la población introducida es incorrecta.")