# pide nombre y edad si es menor de edad da error sino muestra nombre y dice q es mayor de edad.
nombre=str(input("Introduce tu nombre: "))
edad=int(input("Introduce tu edad: "))
while edad<18:
    print("\nEres menor de edad!!!!!!!!")
    nombre=str(input("Introduce tu nombre: "))
    edad=int(input("Introduce tu edad: "))
print("%s es mayor de edad!!" %(nombre))
print("Bienvenido!!!")
