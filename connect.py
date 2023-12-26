import psycopg2

def connectionBD():
    try:
        mydb = psycopg2.connect(
            host='34.29.69.18',
            port='5432',
            user='postgres',
            password='lambo123456',
            database='postgres'
        ) 
        print("Conexión exitosa")
        return mydb
    except Exception as e:
        print("Error en la conexión:", repr(e))
        return None

conexion = connectionBD()
if conexion:
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM contactanos;")
    resultados = cursor.fetchall()
    for row in resultados:
        print(row)
    cursor.close()
    conexion.close()
else:
    print("No se pudo establecer la conexión.")
