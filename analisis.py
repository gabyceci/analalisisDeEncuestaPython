import csv

# En esta lista cargaremos los datos de las respuestas de la encuesta
# una vez las ordene
encuestas_estudiantes = []

archivo_encuesta = 'encuesta_ingenieria_10000_respuestas.csv' 

# Abrimos el archivo con la libreria with en modo lectura
with open(archivo_encuesta, mode='r', encoding='utf-8') as archivo:
    # lector sera para manejar el ciclo for
    lector = csv.reader(archivo)
    next(lector)  # Saltamos los encabezados del archivo
    # Sacamos los datos del archivo segun sus ubicaciones
    for fila in lector:
        id_estudiante = fila[0]
        carrera = fila[1]
        semestre = fila[2]
        jornada = fila[3]
        trabaja = fila[4]
        promedio = float(fila[5])
        horas_estudio = int(fila[6])    
        calidad_internet = int(fila[15]) 
        nivel_dificultad = int(fila[20]) 
        nivel_estres = int(fila[21])    

        # Los organizamos segun el tipo de informacion recopilada
        datos_generales = [id_estudiante, carrera, semestre, jornada]
        datos_academicos = [promedio, horas_estudio]
        datos_socio_tecnologicos = [trabaja, calidad_internet]
        datos_psicologicos = [nivel_dificultad, nivel_estres]

        # Organizamos los datos de los estudiante
        # en una lista donde se almacenaran las respuestas
        # ya ordenadas por seccion

        estudiante_encuestado = [
            datos_generales,
            datos_academicos,
            datos_socio_tecnologicos,
            datos_psicologicos
        ]
        
        # Asignamos los estudiantes encuestados en la variable
        # general puesta al principio 
        encuestas_estudiantes.append(estudiante_encuestado)


# REPORTE 5: PROMEDIO DE ESTUDIANTES QUE TRABAJAN Y NO TRABAJAN

si_trabaja = 0
no_trabaja = 0
total_estudiantes = len(encuestas_estudiantes) # para sacar el numero total est encuestados

# Con ciclo for en la variable estudiante recorremos la lista
for estudiante in encuestas_estudiantes:
    # Extraemos la lista en especifico que necesitamos
    estado_laboral = estudiante[2][0].strip().lower()
    
    # Validamos con if los estudiantes que trabajan y los que no
    if estado_laboral in ["si", "sí"]:
        # Se suma un estudiante que si trabaja 
        si_trabaja += 1
        # Se suma un estudiante que no trabaja
    elif estado_laboral == "no":
        no_trabaja += 1
  
print("--- --------REPORTE 5---------- ---")
# Calculamos el promedio exacto
promedio_si = si_trabaja / total_estudiantes
promedio_no = no_trabaja / total_estudiantes

# Lo imprimimos 
print("El Promedio de estudiantes que SI trabajan es:", promedio_si*100,"%")
print("El Promedio de estudiantes que NO trabajan es:", promedio_no*100,"%")

# REPORTE 6: PROMEDIO GENERAL DE NOTAS DE TODOS LOS ALUMNOS

# 1. Variable donde vamos a ir sumando todas las notas de los alumnos
suma_total_notas = 0.0

# 2. Guardamos la cantidad exacta de alumnos encuestados que tenemos 
total_estudiantes = len(encuestas_estudiantes)

# 3. Recorremos la lista 
for estudiante in encuestas_estudiantes:
    
    # Extraemos la nota de la seccion datos academicos
    nota_del_estudiante = estudiante[1][0]
    
    # Le sumamos esta nota a nuestro total
    suma_total_notas += nota_del_estudiante

print("--- ---------REPORTE 6----------------")

# 4. Dividimos la suma entre todos los estudiantes
promedio_general = suma_total_notas / total_estudiantes

# 5. Imprimimos el resultado redondeado a 2 decimales para que se vea como una nota escolar
print("El Promedio General de todos los 10,000 estudiantes es:", (promedio_general, ))
 
 
# PROMEDIO POR CARRERA REPORTE 7
# Declaramos contadores
nota_sistemas = 0.0
cant_sistemas = 0

nota_electrica = 0.0
cant_electrica = 0

nota_electronica = 0.0
cant_electronica = 0

# Con ciclo for realizamos y if condicionamos por carreras las operaciones

for estudiante in encuestas_estudiantes:
    carrera = estudiante[0][1].strip().lower()
    if carrera in ["ingeniería de sistemas","ingenieria de sistemas"] :
        # 1. Sacamos la nota de este estudiante
        nota_actual = estudiante[1][0] 
        
        # La agregamos a la lista al ser un estudiante de sistemas
        nota_sistemas += nota_actual 
        
        # 3. Contamos que es un alumno de sistemas
        cant_sistemas += 1

        # Repetimos proceso con las demas carreras
    elif carrera in ["ingeniería eléctrica","ingenieria electrica"] :
        nota_actual = estudiante[1][0] 
        
        nota_electrica += nota_actual 
        
        # 3. Contamos al alumno de electrica
        cant_electrica += 1
        
    elif carrera in ["ingeniería electrónica","ingenieria electrónica"]:
        nota_actual = estudiante[1][0] 
        
        nota_electronica += nota_actual 
        
        # 3. Contamos al alumno de electronica
        cant_electronica += 1
        
        
# Fuera del ciclo calculamos los promedios 
prom_sistemas = nota_sistemas / cant_sistemas
prom_electrica = nota_electrica / cant_electrica
prom_electronica = nota_electronica / cant_electronica
print("--------REPORTE 7----------")
print("LOS PROMEDIOS POR CARRERA SON:")
print("SISTEMAS:", prom_sistemas, "ELECTRICA:", prom_electrica, "ELECTRONICA:", prom_electronica)

# REPORTE 8: PROMEDIO POR SEMESTRE
# Declaramos contadores
nota_semestre5 = 0.0
cant_semestre5 = 0

nota_semestre6 = 0.0
cant_semestre6 = 0

nota_semestre7 = 0.0
cant_semestre7 = 0

# Repetimos formula anterior
for estudiante in encuestas_estudiantes:
    semestre = estudiante[0][2].strip().lower()
    if semestre in ["5"] :
        # 1. Sacamos la nota
        nota_actual = estudiante[1][0] 
        
        # La agregamos a la lista 
        nota_semestre5 += nota_actual 
        
        # 3. Contamos que es un alumno de 5to semestre
        cant_semestre5 += 1

        # Repetimos proceso con los demas semestres
    elif semestre in ["6"] :
        nota_actual = estudiante[1][0] 
        
        nota_semestre6 += nota_actual 
        
        # 3. Contamos al alumno de semestre 6
        cant_semestre6 += 1
        
    elif semestre in ["7"]:
        nota_actual = estudiante[1][0] 
        
        nota_semestre7 += nota_actual 
        
        # 3. Contamos al alumno del semestre 7
        cant_semestre7 += 1
        
# Fuera del ciclo calculamos los promedios 
prom_semestre5 = nota_semestre5 / cant_semestre5
prom_semestre6 = nota_semestre6 / cant_semestre6
prom_semestre7 = nota_semestre7 / cant_semestre7
print("--------REPORTE 8----------")
print("LOS PROMEDIOS POR SEMESTRE SON:")
print("SEMESTRE 5:", prom_semestre5, "SEMESTRE 6:", prom_semestre6, "SEMESTRE 7:", prom_semestre7)

# Cargar datos para reportes 9-20
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
IDX_DIFICULTAD = encabezado.index('q15_dificultad_cursos')
IDX_ESTRES = encabezado.index('q16_estres_academico')

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

#reporte numero 13: Nivel de estres academico general#

suma_estres = 0 #variable para acumular la suma total#

for fila in datos: #recorrer las respuestas brindadas#
    suma_estres += int(fila[IDX_ESTRES])
    
    promedio_estres = suma_estres / len(datos)
    
    
print("----------------------------------------------------------")
print("reporte 13: NIVEL DE ESTRES ACADEMICO GENERAL")
print(len(datos))  # debe dar 10000
print("el nivel de estres academico promedio de los estudiantes es:", promedio_estres)

if promedio_estres < 2:
    print("Interpretación: Bajo nivel de estrés.")
elif promedio_estres < 4:
    print("Interpretación: Nivel de estrés moderado.")
else:
    print("Interpretación: Alto nivel de estrés.")


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
print("----------------------------------------------------------")
print("\nREPORTE 14: PERCEPCIÓN DE DIFICULTAD DE LOS CURSOS")
print("Nivel de dificultad más frecuente:", max_valor)
print("Interpretación:", descripcion)


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

print("----------------------------------------------------------")
print("\nREPORTE 15: CARRERA CON MAYOR NIVEL DE ESTRÉS")
print("Carrera:", carreras[pos])
print("Nivel de estrés promedio:", round(max_prom, 2))


if max_prom < 2:
    print("Interpretación: Bajo nivel de estrés en esta carrera.")
elif max_prom < 4:
    print("Interpretación: Nivel de estrés moderado en esta carrera.")
else:
    print("Interpretación: Alto nivel de estrés en esta carrera.")

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
print("----------------------------------------------------------")
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
