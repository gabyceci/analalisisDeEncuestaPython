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

#REPORTE 16 RELACION ENTRE TRABAJAR Y PROMEDIO ACADEMICO #
suma_trabaja = 0
conteo_trabaja = 0     #variables para estudiantes que trabajan#

suma_no_trabaja = 0        #variable para estudiantes que no trabajan#
conteo_no_trabaja = 0

for fila in datos:
    # limpiar texto#
    trabaja = fila[IDX_TRABAJA].strip().lower()
    promedio = float(fila[IDX_PROMEDIO])


    if trabaja.startswith("s"):   # detecta "sí", "si", "SI", etc.
        suma_trabaja += promedio
        conteo_trabaja += 1
    else:
        suma_no_trabaja += promedio
        conteo_no_trabaja += 1


# Evitar división entre 0
if conteo_trabaja > 0:
    prom_trabaja = suma_trabaja / conteo_trabaja
else:
    prom_trabaja = 0

if conteo_no_trabaja > 0: 
    prom_no_trabaja = suma_no_trabaja / conteo_no_trabaja
else:
    prom_no_trabaja = 0


# Mostrar resultados
print("\nREPORTE 16: RELACIÓN ENTRE TRABAJAR Y PROMEDIO ACADÉMICO")
print("Cantidad que trabajan:", conteo_trabaja)
print("Cantidad que NO trabajan:", conteo_no_trabaja)

print("Promedio de estudiantes que trabajan:", round(prom_trabaja, 2))
print("Promedio de estudiantes que NO trabajan:", round(prom_no_trabaja, 2))


# Interpretación
if prom_trabaja > prom_no_trabaja:
    print("Interpretación: Los estudiantes que trabajan tienen mejor promedio.")
elif prom_trabaja < prom_no_trabaja:
    print("Interpretación: Los estudiantes que NO trabajan tienen mejor rendimiento académico.")
else:
    print("Interpretación: No hay diferencia significativa entre ambos grupos.")