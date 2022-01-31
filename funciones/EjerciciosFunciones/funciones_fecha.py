#FUNCIONES

def LeerFecha():
    dia=int(input("Día: "))
    mes=int(input("Mes: "))
    año=int(input("Año: "))
    while not ValidarFecha(dia,mes,año):
        print("Fecha incorrecta")
        dia=int(input("Día: "))
        mes=int(input("Mes: "))
        año=int(input("Año: "))
    return dia,mes,año

def EsBisiesto(dato_año):
    return dato_año % 4 == 0

def DiaMes(dato_mes,dato_año):
    meses=[31,28,31,30,31,30,31,31,30,31,30,31]
    if EsBisiesto(dato_año):
        meses[1]=29
    return meses[dato_mes-1]

def CalcularDiaJuliano(dato_dia,dato_mes,dato_año):
    diaj=0
    for mes in range(1,dato_mes):
        diaj=diaj+DiaMes(mes,dato_año)
    diaj=diaj+dato_dia
    return diaj

def ValidarFecha(dato_dia,dato_mes,dato_año):
    if dato_mes<1 or dato_mes>12:
        return False
    if dato_dia<1 or dato_dia>DiaMes(dato_mes,dato_año):
        return False
    return True