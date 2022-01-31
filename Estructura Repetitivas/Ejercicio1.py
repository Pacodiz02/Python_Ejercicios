num = int(input("Introduce un número: "))

acumu=1

for var in range (1, num+1):
    acumu=acumu*var

print("El resultado es" ,acumu)