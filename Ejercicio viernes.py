# Metenmos numeros hasta meter 0. Los numeros positivos en una lista y negativos en otra.
#Nos tiene que decir si hemos metido mas numeros positivos q negativos y muetra las dos listas.
#Decir si las listas tienen elementos repetidos.
listapos=[]
listaneg=[]

num=int(input("Introduce un número "))

while num!=0:
    if num >0:
        listapos.append(num)

    elif num<0:
        listaneg.append(num)

    num=int(input("Introduce un número "))

if len(listapos) > len(listaneg):
    print("Hay más números positivos")
elif len(listaneg) > len(listapos):
    print("Hay más números negativos")
else:
    print("Hay el mismo número de positivos que de negativos")

for num in listapos:
    print(num, end="")
    