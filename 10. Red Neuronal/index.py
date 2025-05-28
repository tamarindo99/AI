# Importamos a nuestra libreta de trabajo las librerias a utilizar
import tensorflow as tf  # libreria para IA desarrollada por google
import numpy as np  # para trabajar con números
import matplotlib.pyplot as plt  # se importa la libreria matplot para hacer las gráficas

# introducimos los datos. Se crea un array, un tipo de dato estructurado que permite almacenar un conjunto de datos homogéneo
celsius = np.array([-40, -10, 0, 8, 15, 22, 38], dtype=float)  # float son números reales con comas, coma flotante
fahrenheit = np.array([-40, 14, 32, 46, 59, 72, 100], dtype=float)  # np es numpy python, números en python

# estos son los ejemplos que la red usará para aprender. De momento no sabemos cual es la fórmula
print("Datos de entrada (Celsius):", celsius)
print("Datos esperados (Fahrenheit):", fahrenheit)

# Modelo de red neuronal con una neurona. Utilizamos el framework Keras.
capa = tf.keras.layers.Dense(units=1, input_shape=[1])  # capa densa con una neurona
print("\nConfiguración de capa simple:", capa)

# Modelo secuencial
modelo = tf.keras.Sequential([capa])  # creamos un modelo secuencial con una capa
print("\nConfiguración del modelo simple:", modelo)

# COMPILAMOS EL MODELO
modelo.compile(
    optimizer=tf.keras.optimizers.Adam(0.1),  # tasa de aprendizaje de 0.1
    loss='mean_squared_error'  # función de pérdida: error cuadrático medio
)

# ENTRENAMIENTO DEL MODELO
print("\nComenzando entrenamiento del modelo simple...")
historial = modelo.fit(celsius, fahrenheit, epochs=1000, verbose=False)
print("Modelo simple entrenado!")

# RESULTADO DE LA FUNCIÓN DE PÉRDIDA
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title("Modelo Simple")
plt.xlabel("# Vuelta dada")
plt.ylabel("Magnitud de pérdida")
plt.plot(historial.history["loss"])

# PREDICCIÓN DEL MODELO
print("\nHagamos una predicción con el modelo simple!")
resultado = modelo.predict(np.array([100.0]).reshape(-1, 1))  # Formato correcto para predicción
print("El resultado es " + str(resultado[0][0]) + " fahrenheit!")

# MOSTRANDO LAS VARIABLES INTERNAS DEL MODELO
print("\nVariables internas del modelo simple:")
pesos, sesgo = capa.get_weights()
print(f"Peso: {pesos[0][0]:.4f} (esperado ~1.8)")
print(f"Sesgo: {sesgo[0]:.4f} (esperado ~32)")

# MODELO CON CAPAS OCULTAS
print("\nCreando modelo con capas ocultas...")
oculta1 = tf.keras.layers.Dense(units=3, input_shape=[1])
oculta2 = tf.keras.layers.Dense(units=3)
salida = tf.keras.layers.Dense(units=1)
modelo_complejo = tf.keras.Sequential([oculta1, oculta2, salida])

modelo_complejo.compile(
    optimizer=tf.keras.optimizers.Adam(0.1),
    loss='mean_squared_error'
)

print("Comenzando entrenamiento del modelo complejo...")
historial_complejo = modelo_complejo.fit(celsius, fahrenheit, epochs=1000, verbose=False)
print("Modelo complejo entrenado!")

# Gráfica de pérdida para el modelo complejo
plt.subplot(1, 2, 2)
plt.title("Modelo Complejo")
plt.xlabel("# Epoca")
plt.ylabel("Magnitud de pérdida")
plt.plot(historial_complejo.history["loss"])
plt.tight_layout()
plt.show()

# PREDICCIÓN DEL MODELO COMPLEJO
print("\nHagamos una predicción con el modelo complejo!")
resultado_complejo = modelo_complejo.predict(np.array([100.0]).reshape(-1, 1))  # Formato correcto para predicción
print("El resultado es " + str(resultado_complejo[0][0]) + " fahrenheit!")

# MOSTRANDO LAS VARIABLES INTERNAS DEL MODELO COMPLEJO
print("\nVariables internas del modelo complejo:")
print("\nCapa oculta 1:")
print("Pesos:", oculta1.get_weights()[0])
print("Sesgos:", oculta1.get_weights()[1])

print("\nCapa oculta 2:")
print("Pesos:", oculta2.get_weights()[0])
print("Sesgos:", oculta2.get_weights()[1])

print("\nCapa de salida:")
print("Pesos:", salida.get_weights()[0])
print("Sesgo:", salida.get_weights()[1][0])