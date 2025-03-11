#Programación asíncrona (async/await)
#Manejo de hilos (threading)
#Manejo de procesos (multiprocessing)
#Manejo de contextos (with)
#Metaclases
#Decoradores avanzados
#Manejo de memoria (weakref)
#Serialización de objetos (pickle)
#Manejo de sockets
#Uso de bibliotecas externas (requests, numpy)

# 1. Programación asíncrona (async/await)
import asyncio

async def tarea_asincrona():
    print("Iniciando tarea asíncrona")
    await asyncio.sleep(2)
    print("Tarea asíncrona completada")

async def main():
    await asyncio.gather(tarea_asincrona(), tarea_asincrona())

asyncio.run(main())

# 2. Manejo de hilos (threading)
import threading

def tarea_hilo():
    print("Hilo ejecutándose")

hilo = threading.Thread(target=tarea_hilo)
hilo.start()
hilo.join()

# 3. Manejo de procesos (multiprocessing)
import multiprocessing

def tarea_proceso():
    print("Proceso ejecutándose")

proceso = multiprocessing.Process(target=tarea_proceso)
proceso.start()
proceso.join()

# 4. Manejo de contextos (with)
class MiContexto:
    def __enter__(self):
        print("Entrando en el contexto")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Saliendo del contexto")

with MiContexto() as contexto:
    print("Dentro del contexto")

# 5. Metaclases
class MiMeta(type):
    def __new__(cls, nombre, bases, dct):
        print(f"Creando clase {nombre}")
        return super().__new__(cls, nombre, bases, dct)

class MiClase(metaclass=MiMeta):
    pass

# 6. Decoradores avanzados
def decorador_con_parametros(parametro):
    def decorador(funcion):
        def wrapper(*args, **kwargs):
            print(f"Decorador con parámetro: {parametro}")
            return funcion(*args, **kwargs)
        return wrapper
    return decorador

@decorador_con_parametros("mi_parametro")
def funcion_decorada():
    print("Función decorada ejecutándose")

funcion_decorada()

# 7. Manejo de memoria (weakref)
import weakref

class MiClaseDebil:
    pass

objeto = MiClaseDebil()
referencia_debil = weakref.ref(objeto)
print("Referencia débil:", referencia_debil())

# 8. Serialización de objetos (pickle)
import pickle

class MiClaseSerializable:
    def __init__(self, valor):
        self.valor = valor

objeto = MiClaseSerializable(10)
serializado = pickle.dumps(objeto)
deserializado = pickle.loads(serializado)
print("Valor deserializado:", deserializado.valor)

# 9. Manejo de sockets
import socket

def servidor_socket():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind(('localhost', 12345))
    servidor.listen(1)
    print("Servidor escuchando en localhost:12345")
    cliente, direccion = servidor.accept()
    print(f"Conexión aceptada desde {direccion}")
    cliente.send(b"Hola desde el servidor")
    cliente.close()

def cliente_socket():
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect(('localhost', 12345))
    mensaje = cliente.recv(1024)
    print("Mensaje recibido:", mensaje.decode())
    cliente.close()

import threading
hilo_servidor = threading.Thread(target=servidor_socket)
hilo_cliente = threading.Thread(target=cliente_socket)
hilo_servidor.start()
hilo_cliente.start()
hilo_servidor.join()
hilo_cliente.join()

# 10. Uso de bibliotecas externas (requests, numpy)
import requests
import numpy as np

# Uso de requests
respuesta = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print("Respuesta de la API:", respuesta.json())

# Uso de numpy
array = np.array([1, 2, 3, 4, 5])
print("Array de numpy:", array)
print("Suma del array:", np.sum(array))




#Programación asíncrona (async/await): Se usa asyncio para ejecutar tareas asíncronas.
#Manejo de hilos (threading): Se crea y ejecuta un hilo para realizar una tarea en paralelo.
#Manejo de procesos (multiprocessing): Se crea y ejecuta un proceso para realizar una tarea en paralelo.
#Manejo de contextos (with): Se define una clase de contexto para manejar recursos.
#Metaclases: Se define una metaclase para personalizar la creación de clases.
#Decoradores avanzados: Se crea un decorador que acepta parámetros.
#Manejo de memoria (weakref): Se usa weakref para crear referencias débiles a objetos.
#Serialización de objetos (pickle): Se serializa y deserializa un objeto usando pickle.
#Manejo de sockets: Se crea un servidor y un cliente de sockets para comunicación en red.
#Uso de bibliotecas externas (requests, numpy): Se usa requests para hacer una solicitud HTTP y numpy para trabajar con arrays.