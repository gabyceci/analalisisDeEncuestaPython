import csv

# Cargar datos
datos = []
encabezado = []

with open("encuesta_ingenieria_10000_respuestas.csv", 'r', encoding='utf-8-sig') as archivo:
    lector = csv.reader(archivo)
    encabezado = next(lector)
    for fila in lector:
        datos.append(fila)

# Indices
IDX_PROMEDIO  = encabezado.index('promedio_actual')
IDX_Q01       = encabezado.index('q01_horas_estudio')
IDX_Q07       = encabezado.index('q07_uso_plataformas')
IDX_Q10       = encabezado.index('q10_calidad_internet')
IDX_Q18       = encabezado.index('q18_satisfaccion_carrera')
IDX_CARRERA   = encabezado.index('carrera')
IDX_SEMESTRE  = encabezado.index('semestre')
IDX_JORNADA   = encabezado.index('jornada')
IDX_TRABAJA   = encabezado.index('trabaja')

total = len(datos)

# Reporte 1
datos_personales = [fila[:6] for fila in datos]        # id, carrera, semestre, jornada, trabaja, promedio
respuestas_q     = [fila[6:] for fila in datos]        # q01 hasta q20

# Reporte
print("=" * 45)
print("  REPORTE 1")
print("=" * 45)
print(f"Total de encuestados : {len(datos)}")
print("=" * 45)

# Reporte 2
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

# Reporte 3
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


# Reporte 4
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

#REPORTE 9
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
 
 
#Reporte 10:
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
 
 
#REPORTE 11:
conteo_horas = {}
for fila in datos:
    nivel = fila[IDX_Q01].strip()
    if nivel in conteo_horas:
        conteo_horas[nivel] += 1
    else:
        conteo_horas[nivel] = 1
 
print("----------------------------------------------------------")
print("  Reporte 11: Horas de estudio semanales")
print("----------------------------------------------------------")
for nivel in sorted(conteo_horas.keys()):
    cantidad = conteo_horas[nivel]
    print(f"  Nivel {nivel} : {cantidad} ({cantidad/total*100:.1f}%)")
print(f"  Total   : {total}")
 
 
#REPORTE 12: Satisfaccion con la carrera 
conteo_satisf = {}
suma_satisf = 0
for fila in datos:
    nivel = fila[IDX_Q18].strip()
    suma_satisf += int(nivel)
    if nivel in conteo_satisf:
        conteo_satisf[nivel] += 1
    else:
        conteo_satisf[nivel] = 1
 
print("----------------------------------------------------------")
print("  REPORTE 12: SATISFACCION CON LA CARRERA")
print("=" * 45)
print(f"  Promedio : {suma_satisf/total:.2f} / 5")
for nivel in sorted(conteo_satisf.keys()):
    cantidad = conteo_satisf[nivel]
    print(f"  Nivel {nivel} : {cantidad} ({cantidad/total*100:.1f}%)")
print(f"  Total    : {total}")


# ── REPORTE 17: Internet vs promedio academico ────────────────
suma_por_internet   = {}
cantidad_por_internet = {}
for fila in datos:
    nivel = fila[IDX_Q10].strip()
    prom  = int(fila[IDX_PROMEDIO])
    if nivel in suma_por_internet:
        suma_por_internet[nivel]    += prom
        cantidad_por_internet[nivel] += 1
    else:
        suma_por_internet[nivel]    = prom
        cantidad_por_internet[nivel] = 1

print("=" * 45)
print("  REPORTE 17: INTERNET VS PROMEDIO ACADEMICO")
print("=" * 45)
for nivel in sorted(suma_por_internet.keys()):
    prom = suma_por_internet[nivel] / cantidad_por_internet[nivel]
    print(f"  Internet nivel {nivel} : promedio {prom:.2f}  (n={cantidad_por_internet[nivel]})")


# ── REPORTE 18: Horas de estudio vs rendimiento ───────────────
suma_por_horas    = {}
cantidad_por_horas = {}
for fila in datos:
    nivel = fila[IDX_Q01].strip()
    prom  = int(fila[IDX_PROMEDIO])
    if nivel in suma_por_horas:
        suma_por_horas[nivel]    += prom
        cantidad_por_horas[nivel] += 1
    else:
        suma_por_horas[nivel]    = prom
        cantidad_por_horas[nivel] = 1

print("=" * 45)
print("  REPORTE 18: HORAS ESTUDIO VS RENDIMIENTO")
print("=" * 45)
for nivel in sorted(suma_por_horas.keys()):
    prom = suma_por_horas[nivel] / cantidad_por_horas[nivel]
    print(f"  Horas nivel {nivel} : promedio {prom:.2f}  (n={cantidad_por_horas[nivel]})")


# ── REPORTE 19: Interes en cursos virtuales ───────────────────
alto_uso = 0
for fila in datos:
    if int(fila[IDX_Q07]) >= 4:
        alto_uso += 1

print("=" * 45)
print("  REPORTE 19: INTERES EN CURSOS VIRTUALES")
print("=" * 45)
print(f"  Interesados     : {alto_uso} ({alto_uso/total*100:.1f}%)")
print(f"  No interesados  : {total - alto_uso} ({(total-alto_uso)/total*100:.1f}%)")
print(f"  Total           : {total}")

# REPORTE 20: Perfil predominante

moda_carrera  = ""
moda_semestre = ""
moda_jornada  = ""
moda_trabaja  = ""
moda_q01      = ""
moda_q10      = ""
moda_q18      = ""

max_carrera  = 0
max_semestre = 0
max_jornada  = 0
max_trabaja  = 0
max_q01      = 0
max_q10      = 0
max_q18      = 0

conteo_carrera  = {}
conteo_semestre = {}
conteo_jornada  = {}
conteo_trabaja  = {}
conteo_q01      = {}
conteo_q10      = {}
conteo_q18      = {}

for fila in datos:
    c = fila[IDX_CARRERA].strip()
    if c in conteo_carrera:
        conteo_carrera[c] += 1
    else:
        conteo_carrera[c] = 1

    s = fila[IDX_SEMESTRE].strip()
    if s in conteo_semestre:
        conteo_semestre[s] += 1
    else:
        conteo_semestre[s] = 1

    j = fila[IDX_JORNADA].strip()
    if j in conteo_jornada:
        conteo_jornada[j] += 1
    else:
        conteo_jornada[j] = 1

    t = fila[IDX_TRABAJA].strip()
    if t in conteo_trabaja:
        conteo_trabaja[t] += 1
    else:
        conteo_trabaja[t] = 1

    q1 = fila[IDX_Q01].strip()
    if q1 in conteo_q01:
        conteo_q01[q1] += 1
    else:
        conteo_q01[q1] = 1

    q10 = fila[IDX_Q10].strip()
    if q10 in conteo_q10:
        conteo_q10[q10] += 1
    else:
        conteo_q10[q10] = 1

    q18 = fila[IDX_Q18].strip()
    if q18 in conteo_q18:
        conteo_q18[q18] += 1
    else:
        conteo_q18[q18] = 1

# Sacar la moda de cada conteo
for carrera, cantidad in conteo_carrera.items():
    if cantidad > max_carrera:
        max_carrera = cantidad
        moda_carrera = carrera

for semestre, cantidad in conteo_semestre.items():
    if cantidad > max_semestre:
        max_semestre = cantidad
        moda_semestre = semestre

for jornada, cantidad in conteo_jornada.items():
    if cantidad > max_jornada:
        max_jornada = cantidad
        moda_jornada = jornada

for trabaja, cantidad in conteo_trabaja.items():
    if cantidad > max_trabaja:
        max_trabaja = cantidad
        moda_trabaja = trabaja

for nivel, cantidad in conteo_q01.items():
    if cantidad > max_q01:
        max_q01 = cantidad
        moda_q01 = nivel

for nivel, cantidad in conteo_q10.items():
    if cantidad > max_q10:
        max_q10 = cantidad
        moda_q10 = nivel

for nivel, cantidad in conteo_q18.items():
    if cantidad > max_q18:
        max_q18 = cantidad
        moda_q18 = nivel

print("=" * 45)
print("  REPORTE 20: PERFIL PREDOMINANTE")
print("=" * 45)
print(f"  Carrera         : {moda_carrera}")
print(f"  Semestre        : {moda_semestre}")
print(f"  Jornada         : {moda_jornada}")
print(f"  Trabaja         : {moda_trabaja}")
print(f"  Horas estudio   : nivel {moda_q01}")
print(f"  Calid. internet : nivel {moda_q10}")
print(f"  Satisfaccion    : nivel {moda_q18}")
print("=" * 45)