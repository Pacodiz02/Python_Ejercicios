#Ejercicio 2

from random import randint

correcto=0
incorrecto=0

rango=int(input("Número de preguntas: "))
for i in range(0,rango):
    
    a=randint(2,10)
    b=randint(2,10)
    multi=a*b
    
    num1=int(input("¿Cuanto es %d por %d? "%(a,b)))

    if num1==multi:
        print("¡Respuesta correcta!")
        correcto=correcto+1
    
    if num1!=multi:
        print("¡Respuesta incorrecta!")
        incorrecto=incorrecto+1

print("Has contestado correctamente %d preguntas."%(correcto))
print("Has tenido %d fallos."%(incorrecto))

nota=correcto/rango*10
print("Has sacado una nota de %d sobre 10"%(nota))

if nota>=9:
    print("¡ENHORABUENA!")
