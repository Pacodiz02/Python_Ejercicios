#Ejercicio 2

from PeliculaEjercicio2 import peliculas

#Muestra el nombre y el argumento de cada película.

for nombreargu in peliculas:
    print(nombreargu.get("title"))
    print(nombreargu.get("storyline"))
    print("\n")

#Muestra el nombre y los actores de cada pélicula.

for namepeli in peliculas:
    print(namepeli.get("title"))
    print(namepeli.get("actors"))

#Pide por teclado un genero y muestra el nombre de las péliculas de ese genero.
print("\n")
genero=input("Dime un género: ")
print("\n")

for gen in peliculas:
    for gen2 in gen.get("genres"):
        if genero == gen2:
            print(gen.get("title"))
            
#Pide un año por teclado y muestra todas las péliculas anteriores a ese año.
print("\n")
años=input("Introduce un año: ")
print("\n")
for año1 in peliculas:
    if años > año1.get("year"):
        print(año1.get("title"))