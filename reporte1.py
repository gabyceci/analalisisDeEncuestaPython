import csv

# Lista principal que contendrá sublistas temáticas
datos = []          # Lista de listas (cada fila es una sublista)
encabezado = []

with open("encuesta_ingenieria_10000_respuestas.csv", 'r', encoding='utf-8-sig') as archivo:
    lector = csv.reader(archivo)
    encabezado = next(lector)
    
    for fila in lector:
        datos.append(fila)  # Cada fila ya ES una sublista

# ── Listas anidadas derivadas de 'datos' ──────────────────
# Aquí se justifica su uso: separar los datos por categoría

datos_personales = [fila[:6] for fila in datos]        # id, carrera, semestre, jornada, trabaja, promedio
respuestas_q     = [fila[6:] for fila in datos]        # q01 hasta q20

# Reporte
print("=" * 45)
print("  REPORTE 1")
print("=" * 45)
print(f"Total de encuestados : {len(datos)}")
print("=" * 45)
# print(f"Columnas: {encabezado[:6]}")
# print(f"Preguntas: {encabezado[6:]}")
# print(f"Ejemplo datos: {datos_personales[0]}")
# print(f"Ejemplo respuestas   : {respuestas_q[0]}")