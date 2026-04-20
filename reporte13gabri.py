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

#reporte numero 13: Nivel de estres academico general#

suma_estres = 0 #variable para acumular la suma total#

for fila in datos: #recorrer las respuestas brindadas#
    suma_estres += int(fila[IDX_ESTRES])
    
    promedio_estres = suma_estres / len(datos)
    
    
print("reporte 13: NIVEL DE ESTRES ACADEMICO GENERAL")
print(len(datos))  # debe dar 10000
print("el nivel de estres academico promedio de los estudiantes es:", promedio_estres)

if promedio_estres < 2:
    print("Interpretación: Bajo nivel de estrés.")
elif promedio_estres < 4:
    print("Interpretación: Nivel de estrés moderado.")
else:
    print("Interpretación: Alto nivel de estrés.")
    
    