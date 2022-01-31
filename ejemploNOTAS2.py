# Con la nota del alumno decir su calificaion

nota = float(input("Pon tu nota: "))

if nota >=1 and nota <= 4:
    print("Insuficiente")

elif nota == 5:
    print("Suficiente")

elif nota == 6 or nota == 7:
    print("Bien")

elif nota == 8:
    print("Notable")

elif nota == 9 or nota == 10:
    print("Sobresaliente")

else:
    print("Nota incorrecta")
print("Programa terminado")