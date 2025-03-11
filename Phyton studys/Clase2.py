#List comprehensions
#Funciones lambda
#Manejo de archivos (lectura y escritura)
#Módulos y paquetes
#Manejo de fechas y horas
#Expresiones regulares
#Generadores
#Decoradores
#Manejo de bases de datos (SQLite)
#Manejo de JSON

# 1. List comprehensions
numeros = [1, 2, 3, 4, 5]
cuadrados = [x**2 for x in numeros]
print("Cuadrados:", cuadrados)

# 2. Funciones lambda
multiplicar = lambda x, y: x * y
print("Multiplicación:", multiplicar(3, 4))

# 3. Manejo de archivos
# Escritura
with open("./Phyton studys/archivo.txt", "w") as archivo:
    archivo.write("Hola, este es un archivo de texto.\n")

# Lectura
with open("./Phyton studys/archivo.txt", "r") as archivo:
    contenido = archivo.read()
    print("Contenido del archivo:", contenido)

# 4. Módulos y paquetes
import math
print("Raíz cuadrada de 16:", math.sqrt(16))

# 5. Manejo de fechas y horas
from datetime import datetime, timedelta
ahora = datetime.now()
print("Fecha y hora actual:", ahora)
manana = ahora + timedelta(days=1)
print("Fecha y hora de mañana:", manana)

# 6. Expresiones regulares
import re
texto = "El correo es usuario@example.com"
patron = r"[\w\.-]+@[\w\.-]+"
coincidencias = re.findall(patron, texto)
print("Correos encontrados:", coincidencias)

# 7. Generadores
def generador_numeros(n):
    for i in range(n):
        yield i

for numero in generador_numeros(5):
    print("Número generado:", numero)

# 8. Decoradores
def mi_decorador(funcion):
    def wrapper():
        print("Algo sucede antes de la función.")
        funcion()
        print("Algo sucede después de la función.")
    return wrapper

@mi_decorador
def decir_hola():
    print("¡Hola!")

decir_hola()

# 9. Manejo de bases de datos (SQLite)
import sqlite3

# Conexión a la base de datos (se crea si no existe)
conexion = sqlite3.connect("./Phyton studys/mi_base_de_datos.db")
cursor = conexion.cursor()

# Crear tabla
cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY, nombre TEXT, edad INTEGER)")

# Insertar datos
cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES (?, ?)", ("Ana", 25))
conexion.commit()

# Consultar datos
cursor.execute("SELECT * FROM usuarios")
filas = cursor.fetchall()
print("Usuarios en la base de datos:", filas)

# Cerrar conexión
conexion.close()

# 10. Manejo de JSON
import json

# Convertir un diccionario a JSON
datos = {"nombre": "Carlos", "edad": 30}
json_datos = json.dumps(datos)
print("Datos en JSON:", json_datos)

# Convertir JSON a diccionario
diccionario = json.loads(json_datos)
print("Diccionario desde JSON:", diccionario)



#List comprehensions: Se crea una lista de cuadrados a partir de una lista de números.
#Funciones lambda: Se define una función anónima para multiplicar dos números.
#Manejo de archivos: Se escribe y lee un archivo de texto.
#Módulos y paquetes: Se importa el módulo math para usar funciones matemáticas.
#Manejo de fechas y horas: Se usa el módulo datetime para trabajar con fechas y horas.
#Expresiones regulares: Se usa el módulo re para buscar patrones en un texto.
#Generadores: Se define un generador que produce números hasta un límite.
#Decoradores: Se crea un decorador para añadir funcionalidad antes y después de una función.
#Manejo de bases de datos: Se usa SQLite para crear una base de datos, insertar y consultar datos.
#Manejo de JSON: Se convierte un diccionario a JSON y viceversa.