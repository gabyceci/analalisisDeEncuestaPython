import csv

# ── Carga de datos ────────────────────────────────────────────
datos = []
encabezado = []

with open("encuesta_ingenieria_10000_respuestas.csv", 'r', encoding='utf-8-sig') as archivo:
    lector = csv.reader(archivo)
    encabezado = next(lector)
    for fila in lector:
        datos.append(fila)

# Índices
IDX_Q01  = encabezado.index('q01_horas_estudio')
IDX_Q07  = encabezado.index('q07_uso_plataformas')
IDX_Q10  = encabezado.index('q10_calidad_internet')
IDX_Q18  = encabezado.index('q18_satisfaccion_carrera')

total = len(datos)


# ── REPORTE 9: Acceso a internet en casa ─────────────────────
con_internet = 0
for fila in datos:
    if int(fila[IDX_Q10]) >= 3:
        con_internet += 1

print("----------------------------------------------------------")
print("  Reporte 9: Acceso a internet en casa")
print("----------------------------------------------------------")
print(f"  Con acceso  : {con_internet} ({con_internet/total*100:.1f}%)")
print(f"  Sin acceso  : {total - con_internet} ({(total-con_internet)/total*100:.1f}%)")
print(f"  Total       : {total}")


# ── REPORTE 10: Computadora propia ───────────────────────────
con_computadora = 0
for fila in datos:
    if int(fila[IDX_Q07]) >= 3:
        con_computadora += 1

print("----------------------------------------------------------")
print("  Reporte 10: Computadora propia")
print("----------------------------------------------------------")
print(f"  Con computadora : {con_computadora} ({con_computadora/total*100:.1f}%)")
print(f"  Sin computadora : {total - con_computadora} ({(total-con_computadora)/total*100:.1f}%)")
print(f"  Total           : {total}")


# ── REPORTE 11: Estudiantes por horas de estudio ─────────────
claves_horas  = []
conteos_horas = []

for fila in datos:
    nivel = fila[IDX_Q01].strip()
    encontrado = -1
    for i in range(len(claves_horas)):
        if claves_horas[i] == nivel:
            encontrado = i
            break
    if encontrado == -1:
        claves_horas.append(nivel)
        conteos_horas.append(1)
    else:
        conteos_horas[encontrado] += 1

# Ordenar por nivel (burbuja)
for i in range(len(claves_horas) - 1):
    for j in range(len(claves_horas) - 1 - i):
        if claves_horas[j] > claves_horas[j + 1]:
            claves_horas[j],  claves_horas[j + 1]  = claves_horas[j + 1],  claves_horas[j]
            conteos_horas[j], conteos_horas[j + 1] = conteos_horas[j + 1], conteos_horas[j]

print("=" * 45)
print("  REPORTE 11: HORAS DE ESTUDIO SEMANAL")
print("=" * 45)
for i in range(len(claves_horas)):
    print(f"  Nivel {claves_horas[i]} : {conteos_horas[i]} ({conteos_horas[i]/total*100:.1f}%)")
print(f"  Total   : {total}")


# ── REPORTE 12: Satisfacción con la carrera ──────────────────
claves_satisf  = []
conteos_satisf = []
suma_satisf    = 0

for fila in datos:
    nivel = fila[IDX_Q18].strip()
    suma_satisf += int(nivel)
    encontrado = -1
    for i in range(len(claves_satisf)):
        if claves_satisf[i] == nivel:
            encontrado = i
            break
    if encontrado == -1:
        claves_satisf.append(nivel)
        conteos_satisf.append(1)
    else:
        conteos_satisf[encontrado] += 1

# Ordenar
for i in range(len(claves_satisf) - 1):
    for j in range(len(claves_satisf) - 1 - i):
        if claves_satisf[j] > claves_satisf[j + 1]:
            claves_satisf[j],  claves_satisf[j + 1]  = claves_satisf[j + 1],  claves_satisf[j]
            conteos_satisf[j], conteos_satisf[j + 1] = conteos_satisf[j + 1], conteos_satisf[j]

print("=" * 45)
print("  REPORTE 12: SATISFACCION CON LA CARRERA")
print("=" * 45)
print(f"  Promedio : {suma_satisf/total:.2f} / 5")
for i in range(len(claves_satisf)):
    print(f"  Nivel {claves_satisf[i]} : {conteos_satisf[i]} ({conteos_satisf[i]/total*100:.1f}%)")
print(f"  Total    : {total}")