import csv

# En esta lista cargaremos los datos de las respuestas de la encuest
# una vez las ordene
encuestas_estudiantes = []


archivo_encuesta = 'encuesta_ingenieria_10000_respuestas.csv' 
 
 #abrimos el archivo con la libreria with en modo lectura
with open(archivo_encuesta, mode='r', encoding='utf-8') as archivo:
    #lector sera para manejar el ciclo for
    lector = csv.reader(archivo)
    next(lector)  # Saltamos los encabezados del archivo
 #sacamos los datos del archivo segun sus ubicaciones
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

       #los organizamos segun el tipo de informacion recopilada
        datos_generales = [id_estudiante, carrera, semestre, jornada]
        datos_academicos = [promedio, horas_estudio]
        datos_socio_tecnologicos = [trabaja, calidad_internet]
        datos_psicologicos = [nivel_dificultad, nivel_estres]

        #organizamos los datos de los estudiante
        #en una lista donde se almacenaran las respuestas
        #ya ordenadas por seccion

        estudiante_encuestado = [
            datos_generales,
            datos_academicos,
            datos_socio_tecnologicos,
            datos_psicologicos
        ]
        
        #asinamos los estudiantes encuestados en la variable
        #  general puesta al principio 
        encuestas_estudiantes.append(estudiante_encuestado)
        

# REPORTE 5: PROMEDIO DE ESTUDIANTES QUE TRABAJAN Y NO TRABAJAN

si_trabaja = 0
no_trabaja = 0
total_estudiantes = len(encuestas_estudiantes) #para sacar el numero total est encuestados

#con ciclo for en la variabe estudiante recorremos la lista
for estudiante in encuestas_estudiantes:
    # Extraemos la lisa en especiico que necestiamos
    estado_laboral = estudiante[2][0].strip().lower()
    
    #validamos con if los estudiantes que trabajan y los que no
    if estado_laboral in ["si", "sí"]:
        #se suma un estudiante que si trabaja 
        si_trabaja += 1
        #se suma un estudiante que no trabaja
    elif estado_laboral == "no":
        no_trabaja += 1
  
print("--- --------REPORTE 5---------- ---")
# Calculamos el promedio exacto
promedio_si = si_trabaja / total_estudiantes
promedio_no = no_trabaja / total_estudiantes

# Lo imprimimos 
print("El Promedio de estudiantes que SI trabajan es:", promedio_si*100,"%")
print("El Promedio de estudiantes que NO trabajan es:", promedio_no*100,"%")

# REPORTE:¿ 6 PROMEDIO GENERAL DE NOTAS DE TODOS LOS ALUMNOS


# 1. variable  donde vamos a ir sumando todas las notas de los alumnos
suma_total_notas = 0.0

# 2. Guardamos la cantidad exacta de alumnos encuestados que tenemos 
total_estudiantes = len(encuestas_estudiantes)

# 3. recorremos la lista 
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
 
 
 #PROMEDIO POR CARRERA REPORTE 7
 #declaramos contadores
nota_sistemas = 0.0
cant_sistemas = 0

nota_electrica = 0.0
cant_electrica = 0

nota_electronica = 0.0
cant_electronica = 0
 #con ciclo for realizamos y if condicionamos por carreras las 
 #operaciones

for estudiante in encuestas_estudiantes:
    carrera=estudiante[0][1].strip().lower()
    if carrera in ["ingeniería de sistemas","ingenieria de sistemas"] :
        # 1. Sacamos la nota de este estudiante
        nota_actual = estudiante[1][0] 
        
        #la agregamos a la lista al ser un estudiate de sistemas
        nota_sistemas += nota_actual 
        
        # 3. Contamos que es un alumno de sistemas
        cant_sistemas += 1

        #repetimos proceso con las demas carreras
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
        
        

#fuera del ciclo calculamos los promedios 
prom_sistemas = nota_sistemas / cant_sistemas
prom_electrica = nota_electrica / cant_electrica
prom_electronica = nota_electronica / cant_electronica
print("--------REPORTE 7----------")
print("LOS PROMEDIOS POR CARERA SON:")
print("SISTEMAS:", prom_sistemas, "ELECTRICA:", prom_electrica, "ELECTRONICA:", prom_electronica)

#REPORTE 8--- PROMEDIO POR SEMESTRREE
#declaramos contadores
nota_semestre5 = 0.0
cant_semestre5 = 0

nota_semestre6 = 0.0
cant_semestre6 = 0

nota_semestre7 = 0.0
cant_semestre7 = 0

#repetimos formula anterior
for estudiante in encuestas_estudiantes:
    semestre=estudiante[0][2].strip().lower()
    if semestre in ["5"] :
        # 1. Sacamos la nota
        nota_actual = estudiante[1][0] 
        
        #la agregamos a la lista 
        nota_semestre5 += nota_actual 
        
        # 3. Contamos que es un alumno de 5to semestre
        cant_semestre5+= 1

        #repetimos proceso con los demas semestres
    elif semestre in ["6"] :
        nota_actual = estudiante[1][0] 
        
     
        nota_semestre6 += nota_actual 
        
        # 3. Contamos al alumno de  semestre 6
        cant_semestre6 += 1
        
    elif semestre in ["7"]:
        nota_actual = estudiante[1][0] 
        
        
        nota_semestre7 += nota_actual 
        
        # 3. Contamos al alumno del semestre 7
        cant_semestre7 += 1
        
#fuera del ciclo calculamos los promedios 
prom_semestre5= nota_semestre5 / cant_semestre5
prom_semestre6 = nota_semestre6 / cant_semestre6
prom_semestre7 = nota_semestre7/ cant_semestre7
print("--------REPORTE 8----------")
print("LOS PROMEDIOS POR SEMESTRE SON:")
print("SEMESTRE 5:", prom_semestre5, "SEMESTRE 6:", prom_semestre6, "SEMESTRE 7:", prom_semestre7)
      