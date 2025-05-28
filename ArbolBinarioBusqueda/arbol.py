class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

class Arbol:
    def __init__(self):
        self.raiz = None
    
    def vacio(self):
        return self.raiz is None
    
    def insertar(self, valor):
        if self.vacio():
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)
    
    def _insertar_recursivo(self, nodo_actual, valor):
        if valor < nodo_actual.valor:
            if nodo_actual.izquierdo is None:
                nodo_actual.izquierdo = Nodo(valor)
            else:
                self._insertar_recursivo(nodo_actual.izquierdo, valor)
        elif valor > nodo_actual.valor:
            if nodo_actual.derecho is None:
                nodo_actual.derecho = Nodo(valor)
            else:
                self._insertar_recursivo(nodo_actual.derecho, valor)
    
    def buscar_nodo(self, valor):
        return self._buscar_recursivo(self.raiz, valor)
    
    def _buscar_recursivo(self, nodo_actual, valor):
        if nodo_actual is None or nodo_actual.valor == valor:
            return nodo_actual
        if valor < nodo_actual.valor:
            return self._buscar_recursivo(nodo_actual.izquierdo, valor)
        else:
            return self._buscar_recursivo(nodo_actual.derecho, valor)

def main():
    # Crear un árbol binario de búsqueda
    arbol = Arbol()

    # Insertar nodos
    arbol.insertar(50)
    arbol.insertar(30)
    arbol.insertar(70)
    arbol.insertar(20)
    arbol.insertar(40)
    arbol.insertar(60)
    arbol.insertar(80)

    # Buscar un nodo
    nodo = arbol.buscar_nodo(40)
    if nodo is not None:
        print(f"Nodo encontrado: {nodo.valor}")
    else:
        print("Nodo no encontrado")

    # Verificar si el árbol está vacío
    print(f"¿El árbol está vacío? {arbol.vacio()}")

if __name__ == "__main__":
    main()