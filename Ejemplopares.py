num=int(input("Introduce un número: "))
num2=int(input("Introduce otro número: "))
contador=0

suma=num+num2
acomu=0

if num >= num2:
    print("Números incorrectos")

while num<=num2:
    if num %2 == 0:
        print("El número par es:" ,num)
        contador=contador+1
        acomu=acomu +num
    num=num+1

#for cont in range(num,num2+1):
 #   if cont % 2 == 0:
  #      contador=contador+1
   #     acomu=acomu+contador

print("Has introducido",contador,"números pares y su suma es: ",suma)
