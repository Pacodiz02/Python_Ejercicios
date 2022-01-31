#Agenda de contactos Nombre y Teléfono

contacto={}
agenda=[]

pregunta=input("¿Quieres introducir un contacto(S/N)? ")

while pregunta!="S" or pregunta!="N":
    print("Error en la respuesta")
    pregunta=input("¿Quieres introducir un contacto(S/N)? ")

while pregunta!="N":
    nombre=input("Introduce el nombre: ") 
    telefono=input("Introduce el número de teléfono: ")
    contacto={"Nombre":nombre,"Teléfono":telefono}
    agenda.append(contacto)
    
    pregunta=input("¿Quieres introducir otro contacto(S/N)? ")
    while pregunta!="S" or pregunta!="N":
        print("Error en la respuesta")
        pregunta=input("¿Quieres introducir otro contacto(S/N)? ")

#Mostrar todos nombres y telefonos

for a in agenda:
    print("Nombre del contacto: ", a.get("nombre"))
    print("Telefono del contacto: ", a.get("telefono"))


#Mostrar cunatos contactos tiene la agenda

print(len(agenda))


#Pedir un nombre y si existe el contacto mostrar su teléfono y sino existe indicarlo.

nom=input("Introduce un nombre de un contacto: ")

for i in agenda:
    





