import oracledb
from conexion import obtener_conexion

try:
    with obtener_conexion() as conexion:
        print("Conexion exitosa con Oracle Database")
        print("Usuario:", conexion.username)
        print("Version de Oracle:", conexion.version)

except oracledb.Error as error:
    print("Error al conectar con Oracle:")
    print(error)