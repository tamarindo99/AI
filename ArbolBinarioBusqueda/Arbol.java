package ArbolBinarioBusqueda;

public class Arbol {
    
    private Nodo raiz;

    public Arbol() {
        this.raiz = null;
    }

    public boolean vacio() {
        return raiz == null;
    }

    public void insertar(int valor) {
        if (vacio()) {
            raiz = new Nodo(valor);
        } else {
            insertarRecursivo(raiz, valor);
        }
    }

    private void insertarRecursivo(Nodo nodoActual, int valor) {
        if (valor < nodoActual.valor) {
            if (nodoActual.izquierdo == null) {
                nodoActual.izquierdo = new Nodo(valor);
            } else {
                insertarRecursivo(nodoActual.izquierdo, valor);
            }
        } else if (valor > nodoActual.valor) {
            if (nodoActual.derecho == null) {
                nodoActual.derecho = new Nodo(valor);
            } else {
                insertarRecursivo(nodoActual.derecho, valor);
            }
        }
    }

    public Nodo buscarNodo(int valor) {
        return buscarRecursivo(raiz, valor);
    }

    private Nodo buscarRecursivo(Nodo nodoActual, int valor) {
        if (nodoActual == null || nodoActual.valor == valor) {
            return nodoActual;
        }
        if (valor < nodoActual.valor) {
            return buscarRecursivo(nodoActual.izquierdo, valor);
        } else {
            return buscarRecursivo(nodoActual.derecho, valor);
        }
    }
}
