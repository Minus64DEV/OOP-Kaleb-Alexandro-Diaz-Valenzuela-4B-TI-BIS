import mysql.connector
from mysql.connector import Error
from .config import DB_config  

class Database_connection:
    def __init__(self):
        self.config = DB_config 

    def get_connection(self):
        print(self.config)
        try:
            conexion = mysql.connector.connect(**self.config)
            if conexion.is_connected():
                return conexion
        except Error as e:
            print(f"Error al conectar con MySQL: {e}")
            return None

    def ejecutar_consulta(self, query, params=()):
            conexion = self.get_connection()
            if not conexion:
                return None
            
            cursor = conexion.cursor(dictionary=True)
            try:
                cursor.execute(query, params)
            
                if query.strip().upper().startswith(("INSERT", "UPDATE", "DELETE")):
                    conexion.commit()
                    result = cursor.lastrowid 
                else:
                    result = cursor.fetchall() 
                    
            except Error as e:
                print(f"Error al ejecutar la consulta: {e}")
                result = None
            finally:
                cursor.close()
                conexion.close()
                
            return result

