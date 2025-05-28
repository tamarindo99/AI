import numpy as np

class Perceptron:
    def __init__(self, tasa_aprendizaje=0.01, n_epocas=50):
        """
        Inicializa el perceptrón
        
        Parámetros:
        tasa_aprendizaje (float): Tasa de aprendizaje (entre 0.0 y 1.0)
        n_epocas (int): Número de pasadas sobre el conjunto de entrenamiento
        """
        self.tasa_aprendizaje = tasa_aprendizaje
        self.n_epocas = n_epocas
        self.pesos = None
        self.sesgo = None
    
    def funcion_activacion(self, x):
        """Función de activación escalón unitario"""
        return 1 if x >= 0 else 0
    
    def predict(self, x):
        """Realiza una predicción para una sola muestra"""
        suma_ponderada = np.dot(x, self.pesos) + self.sesgo
        return self.funcion_activacion(suma_ponderada)
    
    def fit(self, X, y):
        """
        Entrena el modelo perceptrón
        
        Parámetros:
        X (array): Matriz de características de entrenamiento (n_muestras, n_características)
        y (array): Vector de etiquetas objetivo (n_muestras)
        """
        # Inicializar pesos pequeños aleatorios y sesgo a cero
        n_caracteristicas = X.shape[1]
        self.pesos = np.random.randn(n_caracteristicas) * 0.01
        self.sesgo = 0
        
        # Lista para guardar errores por época
        errores_por_epoca = []
        
        for _ in range(self.n_epocas):
            errores = 0
            for xi, etiqueta in zip(X, y):
                # Calcular predicción
                prediccion = self.predict(xi)
                
                # Actualizar pesos y sesgo
                actualizacion = self.tasa_aprendizaje * (etiqueta - prediccion)
                self.pesos += actualizacion * xi
                self.sesgo += actualizacion
                
                # Contar errores
                errores += int(actualizacion != 0.0)
            
            errores_por_epoca.append(errores)
        
        return errores_por_epoca
    
# Datos de ejemplo (OR lógico)
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 1, 1, 1])

# Crear y entrenar el perceptrón
perceptron = Perceptron(tasa_aprendizaje=0.1, n_epocas=10)
errores = perceptron.fit(X, y)

# Mostrar evolución de errores
print("Errores por época:", errores)

# Probar el modelo entrenado
print("Predicciones:")
for xi in X:
    print(f"{xi} -> {perceptron.predict(xi)}")

# Mostrar pesos finales
print("Pesos finales:", perceptron.pesos)
print("Sesgo final:", perceptron.sesgo)