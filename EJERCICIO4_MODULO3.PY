import mysql.connector
###INSERTAR DATOA A LA TABLA PELICULAS DE LA BBDD DE CINE
conexion = mysql.connector.connect(user="root",password="",host="localhost",database="cine")
cursor =conexion.cursor()

cursor.execute("SELECT Título FROM película")

for fila in cursor:
    print(fila)

conexion.close()