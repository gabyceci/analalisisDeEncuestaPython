import csv 

datos = []
encabezado = []


with open("encuesta_ingenieria_10000_respuestas.csv", 'r', encoding="utf-8-sig") as archivo:
    lector = csv.reader(archivo)
    encabezado = next(lector)

    for fila in lector:
        datos.append(fila)

# Indice de la columna jornada 
IDX_JORNADA = encabezado.index('jornada')

# Contar estudiantes por jornada
conteo_jornada = {}

for fila in datos:
    jornada = fila[IDX_JORNADA].strip()

    if jornada in conteo_jornada:
        conteo_jornada[jornada] += 1
    else:
        conteo_jornada[jornada] = 1

# Resultados
print("=" * 45)
print("  REPORTE 4 ")
print("CANTIDAD DE ESTUDIANTES POR JORNADA")
print("=" * 45)
for jornada, cantidad in conteo_jornada.items():
    porcentaje = (cantidad / len(datos)) * 100
    print(f"Jornada {jornada:<5} : {cantidad} ({porcentaje:.1f}%)")
print("=" * 45)
print(f"  Total                          : {len(datos)}")