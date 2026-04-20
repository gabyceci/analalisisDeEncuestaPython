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


#reporte 14: Curso percibido como mas dificil#

conteo_dificultad= [0]*6 #en escala de 1 a 5

for fila in datos:             #recorrer datos#
    valor= int(fila[IDX_DIFICULTAD])
    conteo_dificultad[valor] += 1
#obtener el nivel mas frecuente#
max_valor = conteo_dificultad.index(max(conteo_dificultad))

# Interpretación del nivel
if max_valor == 1:
    descripcion = "Muy fácil"
elif max_valor == 2:
    descripcion = "Fácil"
elif max_valor == 3:
    descripcion = "Moderado"
elif max_valor == 4:
    descripcion = "Difícil"
else:
    descripcion = "Muy difícil"

# Mostrar resultados
print("\nREPORTE 14: PERCEPCIÓN DE DIFICULTAD DE LOS CURSOS")
print("Nivel de dificultad más frecuente:", max_valor)
print("Interpretación:", descripcion)