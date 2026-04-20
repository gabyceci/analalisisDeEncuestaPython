import csv

# Lista principal que contendrá sublistas temáticas
datos = []          # Lista de listas (cada fila es una sublista)
encabezado = []

with open("encuesta_ingenieria_10000_respuestas.csv", 'r', encoding='utf-8-sig') as archivo:
    lector = csv.reader(archivo)
    encabezado = next(lector)
    
    for fila in lector:
        datos.append(fila)  # Cada fila ya ES una sublista

# Índice de la columna carrera
IDX_CARRERA = encabezado.index('carrera')

# Contar estudiantes por carrera usando un diccionario
conteo_carreras = {}

for fila in datos:
    carrera = fila[IDX_CARRERA].strip()
    
    if carrera in conteo_carreras:
        conteo_carreras[carrera] += 1      # Si ya existe, suma 1
    else:
        conteo_carreras[carrera] = 1       # Si no existe, lo crea con 1

# Mostrar resultados
print("=" * 45)
print("  REPORTE 2 ")
print("  CANTIDAD DE ESTUDIANTES POR CARRERA")
print("=" * 45)
for carrera, cantidad in conteo_carreras.items():
    porcentaje = (cantidad / len(datos)) * 100
    print(f"  {carrera:<30} : {cantidad} ({porcentaje:.1f}%)")
print("=" * 45)
print(f"  Total                          : {len(datos)}")