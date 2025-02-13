# db/connection.py
import mysql.connector
from mysql.connector import Error

def get_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",         # Usuario por defecto en XAMPP
            password="",         # Si tienes contraseña, ingrésala aquí
            database="crud_db"   # Asegúrate de haber creado esta base de datos
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print("Error al conectar a la base de datos:", e)
        return None
