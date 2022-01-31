#Ejercicio3
#Crea un programa python con un diccionario que tenga el contenido del fichero metallica.txt

from Metalica import metalica

cont=0
cont1=0

#Numero de discos.
for album in metalica:
    cont+=1
print("Numero de discos:" ,cont)


#El nombre de todos los discos de Metallica,el número de canciones que tiene cada uno y el número de reproducciones que ha tenido.
for album in metalica:
    print("\n")
    print(album.get("album").get("name"))
    pos = metalica.index(album)

    for can in metalica[pos].get("album").get("tracks").get("track"):
        cont1+=1
    print("Tiene %s canciones." %(cont1))
    cont1=0

    print("Tiene %s reproducciones." %(album.get("album").get("playcount")))
    

#Pide por teclado el nombre de un disco y muestra el título de las canciones. Si no existe el disco da un error.

print("\n")
nombredisc=input("Dime el nombre de un disco: ")
print("\n")

for nom in metalica:
    if nombredisc == nom.get("album").get("name"):
        for titulo in nom.get("album").get("tracks").get("track"):
            print(titulo.get("name"))
    else:
        print("No existe el disco.")
#Pide por teclado una etiqueta y muestra los títulos de los discos que tiene esa etiqueta y las urls donde encontramos las imágenes.

etiqueta=input("Dime una etiqueta: ")

check1=False

for etiq in metalica:
    for titulo in etiq.get("album").get("tags").get("tag"):
        if etiqueta == titulo.get("name"):
            print(etiq.get("album").get("name"))
            print("La URL es: ",titulo.get("url"))