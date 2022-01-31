#ANALISIS
#Definición del problema: Tenemos que pedir la hora de salida (hora, minutos y segundos). Tengo que saber también el tiempo en segundo que ha tardado en llegar. Tenemos que calcular la hora de llegada.
#Datos/Variables de entrada: hora_salida (entero), minutos_salida (entero), segundos_salida (entero), segundos_viaje (entero).
#Datos/variables de salida: hora_llegada (entero), minutos_llegada (entero), segundos_llegada (entero)
#
#DISEÑO
#Leer hora_salida,minutos_salida, segundos_salida
#Leer segundos_viaje
#Convierto la hora de salida a segundos (necesito una variable seginicial) seginicial=hora_salida * 3600 + minuto_salida * 60 + segundos_salida
#Le sumo los segundos que he tardado(necesito una variable segfinal) `segfinal=seginial+segundos_viaje
#Convierto los segundos totales a hora, minuto y segundos horallegada = (segfinal / 3600) División entera minllegada = ((segfinal % 3600) / 60) División entera segllegada <- (segfinal % 3600) % 60
#Muestro hora_llegada,minutos_llegada, segundos_llegada

horasalida=int(input("Introduce la hora de salida: "))
minutossalida=int(input("Introduce los minutos de salida: "))
segundossalida=int(input("Introduce los segundos de salida: "))
segundosviaje=int(input("Introduce los segundos de viaje: "))
segundossalida=horasalida*3600+minutossalida*60+segundossalida
