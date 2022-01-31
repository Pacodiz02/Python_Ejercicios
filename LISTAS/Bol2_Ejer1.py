import abc


lista=[]
palabra=input("Introduce una palabra: ")

while palabra !=" ":
    lista.append(palabra)
    palabra=input("Introduce una palabra: ")

palabra_buscar=input("Introduce la palabra a buscar: ")
palabra_sustituir=input("Introduce la palabra a reemplazar: ")

posicion=0

for palabras in lista:
    if palabra_buscar==palabras:
        lista[posicion]=palabra_sustituir
    posicion*=1

for palabras in lista:
    print(palabras, end=" ")
print()
