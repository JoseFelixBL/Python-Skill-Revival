"""
File I/O & CSV Processing

    Read a CSV file (e.g., data.csv with columns Name, Age, City).
    Calculate the average age.
    Find all people from a specific city.
    Write the results to a new text file. Use the csv module.

    Example data from ![Datablist](https://www.datablist.com/learn/csv/download-sample-csv-files)

    Con los datos que tengo no tengo la ciudad ni la edad, pero sí 
    la fecha de nacimiento, así puedo calcular (aprox.) la edad.

    En vez de ver la moda de la ciudad, la veré de los job title, y los 3 primeros.
"""

import csv
import datetime
from collections import Counter

sex = []
dob = []
job_title = []
# extraer datos
with open("people-1000.csv", newline="", encoding="utf-8",) as f:
    lector = csv.DictReader(f)
    for fila in lector:
        sex.append(fila["Sex"])
        dob.append(fila["Date of birth"])
        job_title.append(fila["Job Title"])

# Procesar las fechas en edades
today = datetime.date.today()
t_d = today.day
t_m = today.month
t_y = today.year
edad = []
for fecha in dob:
    a, m, d = fecha.split('-')
    edad.append(int((datetime.datetime(t_y, t_m, t_d) - datetime.datetime(int(a), int(m), int(d))).days / 365.25))

# Sacar stats.
edad_promedio = int(sum(edad) / len(edad))

job_t_mas_comun = Counter(job_title).most_common(3)

print(f"Edad promedio: {edad_promedio}")
print(f"Trabajo más común: {job_t_mas_comun}")
