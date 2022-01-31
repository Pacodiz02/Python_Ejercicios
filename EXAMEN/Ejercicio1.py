#Ejercicio 1

rango=int(input("Introduce el número de edades que vas a introducir: "))

while rango <=0:
    print("La edad debe ser mayor a 0 años.")
    rango=int(input("Introduce el número de edades que vas a introducir: "))

cont=0
total=0
menor=0

for i in range(0,rango):

    edades=int(input("Introdce la edad: "))
  
    while edades <=0 or edades >100:
        print("¡¡La edad no es correcta!!")
        edades=int(input("Introdce la edad: "))
    
    if edades<18:   
        cont =cont+1
        
    if edades<menor:
        menor=edades
    total =total+edades

media=total/rango
    
print("La edad media es: ",media)
print("La edad menor que se ha introducido es: ",menor)
print("Se han introducido %d edad/es menores de 18 años"%(cont))


    

