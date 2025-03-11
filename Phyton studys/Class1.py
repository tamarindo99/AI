#Variables y tipos de datos
#Entrada y salida de datos
#Estructuras de control (if, else, elif)
#Bucles (for, while)
#Funciones
#Listas
#Diccionarios
#Manejo de excepciones
#Clases y objetos (Programación Orientada a Objetos)

# 1. Variables y tipos de datos
nombre = "Juan"
edad = 25
altura = 1.75
es_estudiante = True

# 2. Entrada y salida de datos
print("Hola, " + nombre + "!")
edad_usuario = int(input("¿Cuántos años tienes? "))
print(f"Tienes {edad_usuario} años.")

# 3. Estructuras de control
if edad_usuario >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

# 4. Bucles
print("Contando hasta 5:")
for i in range(1, 6):
    print(i)

print("Contando hasta 5 con while:")
contador = 1
while contador <= 5:
    print(contador)
    contador += 1

# 5. Funciones
def saludar(nombre):
    return f"Hola, {nombre}!"

print(saludar("Ana"))

# 6. Listas
frutas = ["manzana", "banana", "cereza"]
print("Frutas en la lista:")
for fruta in frutas:
    print(fruta)

# 7. Diccionarios
persona = {
    "nombre": "Carlos",
    "edad": 30,
    "ciudad": "Madrid"
}
print(f"{persona['nombre']} vive en {persona['ciudad']}.")

# 8. Manejo de excepciones
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("No se puede dividir por cero.")

# 9. Clases y objetos (POO)
class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def describir(self):
        return f"Coche: {self.marca} {self.modelo}"

mi_coche = Coche("Toyota", "Corolla")
print(mi_coche.describir())