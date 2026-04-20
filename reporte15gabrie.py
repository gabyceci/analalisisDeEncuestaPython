import csv

#letura de archivo#

datos = []

with open("encuesta_ingenieria_10000_respuestas.csv") as archivo:
    lector= csv.reader(archivo)
    encabezado= next(lector) #saltar encabezado#
    
    for fila in lector:
        datos.append(fila)
        
    
#Indices#
IDX_CARRERA = 1
IDX_TRABAJA = 4
IDX_PROMEDIO = 5
IDX_DIFICULTAD = 20
IDX_ESTRES = 21

#REPORTE 15: cARRERA CON MAYOR NIVEL PROMEDIO DE ESTRES#

#listas para almacenar informacion por carrera#
carreras = []
suma_estres_carrera = []
conteo_carrera = []

for fila in datos:
    carrera = fila[IDX_CARRERA]  #obtener carrera#
    estres = int(fila[IDX_ESTRES]) #convertir estres a numero#
    
    if carrera not in carreras:   #si la carrera no esta guardada aun#
        carreras.append(carrera)          #guardar carrera#
        suma_estres_carrera.append(estres)   #iniciar suma#
        conteo_carrera.append(1)             #iniciar conteo#
    else:
        i= carreras.index(carrera)   #buscar donde esta la carrera#
        suma_estres_carrera[i] += estres
        conteo_carrera[i] += 1

#lista para guardar promedios por carrera#
promedios = []
#calcular promedio por carrera#
for i in range(len(carreras)):
    if conteo_carrera[i] != 0:
        promedios.append(suma_estres_carrera[i] / conteo_carrera[i])
    else:
        promedios.append(promedio) # type: ignore
        
#buscar la carrera con mayor promedio de estres#
max_prom = max(promedios)
pos = promedios.index(max_prom)

#mostrar resultados#

print("\nREPORTE 15: CARRERA CON MAYOR NIVEL DE ESTRÉS")
print("Carrera:", carreras[pos])
print("Nivel de estrés promedio:", round(max_prom, 2))


if max_prom < 2:
    print("Interpretación: Bajo nivel de estrés en esta carrera.")
elif max_prom < 4:
    print("Interpretación: Nivel de estrés moderado en esta carrera.")
else:
    print("Interpretación: Alto nivel de estrés en esta carrera.")