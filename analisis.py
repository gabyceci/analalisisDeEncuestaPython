import csv

def analizar_datos(file_diccionario='diccionario_variables_encuesta.csv', file_encuesta='encuesta_ingenieria_10000_respuestas.csv'):
    # Leer el diccionario de variables
    with open(file_diccionario, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        diccionario_variables = {row['variable']: row['descripcion'] for row in reader}

    # Leer las respuestas de la encuesta
    with open(file_encuesta, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        respuestas = list(reader)


    return analisis_resultados