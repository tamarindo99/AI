# Importar librerías
import tensorflow as tf
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt
import numpy as np

# 1. Cargar y preparar datos MNIST
(X_train, y_train), (X_test, y_test) = tf.keras.datasets.mnist.load_data()
X_train = X_train.reshape(-1, 784) / 255.0  # Aplanar imágenes (28x28 -> 784) y normalizar
X_test = X_test.reshape(-1, 784) / 255.0

# 2. Crear modelo de red neuronal densa (no convolucional)
model = models.Sequential([
    layers.Dense(128, activation='relu', input_shape=(784,)),  # Capa oculta
    layers.Dropout(0.2),  # Regularización
    layers.Dense(10, activation='softmax')  # Capa de salida (10 clases)
])

# 3. Compilar y entrenar
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
history = model.fit(X_train, y_train, epochs=10, validation_data=(X_test, y_test))

# 4. Evaluar
test_loss, test_acc = model.evaluate(X_test, y_test, verbose=0)
print(f"\nPrecisión en test: {test_acc:.4f}")

# 5. Mostrar 3 ejemplos aleatorios con predicciones
plt.figure(figsize=(10, 4))
for i in range(3):
    idx = np.random.randint(0, len(X_test))
    plt.subplot(1, 3, i+1)
    plt.imshow(X_test[idx].reshape(28, 28), cmap='gray')
    pred = model.predict(X_test[idx].reshape(1, 784))
    plt.title(f"Pred: {np.argmax(pred)}\nReal: {y_test[idx]}")
    plt.axis('off')
plt.tight_layout()
plt.show()