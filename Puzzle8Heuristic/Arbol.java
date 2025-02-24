package Puzzle8Heuristic;

public class Arbol {

    private Nodo raiz;

    public Arbol() {
        this.raiz = null;
    }

    public Arbol(byte[][] datoRaiz) {
        this.raiz = new Nodo(datoRaiz, 0, 0);
    }

    public Nodo getRaiz() {
        return raiz;
    }

    public void setRaiz(Nodo raiz) {
        this.raiz = raiz;
    }

    public boolean estaVacio() {
        return raiz == null;
    }

    public void agregarNodo(Nodo padre, byte[][] datoHijo, int g, int h) {
        if (padre == null) {
            throw new IllegalArgumentException("El nodo padre no puede ser nulo.");
        }
        Nodo hijo = new Nodo(padre, datoHijo, g, h);
        padre.agregarHijo(hijo);
    }
}

