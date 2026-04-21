import csv


datos = []
encabezado = []

with open("encuesta_ingenieria_10000_respuestas.csv", 'r', encoding="utf-8-sig") as archivo:
    lector = csv.reader(archivo)
    encabezado = next(lector)

    for fila in lector: 
        datos.append(fila)

# Indice de la columna semestre
IDX_SEMESTRE = encabezado.index('semestre')

# Contar estudiantes por el semestre
conteo_semestres = {}

for fila in datos:
    semestre = fila[IDX_SEMESTRE].strip()

    if semestre in conteo_semestres:
        conteo_semestres[semestre] += 1
    else:
        conteo_semestres[semestre] = 1
    
# Resultados
print("=" * 45)
print("  REPORTE 3 ")
print("CANTIDAD DE ESTUDIANTES POR SEMESTRE")
print("=" * 45)
for semestre, cantidad in conteo_semestres.items():
    porcentaje = (cantidad / len(datos)) * 100
    print(f"Semestre {semestre:<5} : {cantidad} ({porcentaje:.1f}%)")
print("=" * 45)
print(f"  Total                          : {len(datos)}")