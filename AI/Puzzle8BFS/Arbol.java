package Puzzle8BFS;

import java.util.ArrayList;
import java.util.List;

public class Arbol {

    private Nodo raiz;

    public Arbol() {
        this.raiz = null;
    }

    public Arbol(byte[][] datoRaiz) {
        this.raiz = new Nodo(datoRaiz);
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

    public void agregarNodo(Nodo padre, byte[][] datoHijo) {
        if (padre == null) {
            throw new IllegalArgumentException("El nodo padre no puede ser nulo.");
        }
        Nodo hijo = new Nodo(padre, datoHijo);
        padre.agregarHijo(hijo);
    }

    public List<Nodo> obtenerNodosEnProfundidad(int profundidadDeseada) {
        List<Nodo> nodosEnProfundidad = new ArrayList<>();
        obtenerNodosEnProfundidadRecursivo(raiz, 0, profundidadDeseada, nodosEnProfundidad);
        return nodosEnProfundidad;
    }

    private void obtenerNodosEnProfundidadRecursivo(Nodo nodo, int profundidadActual, int profundidadDeseada, List<Nodo> nodosEnProfundidad) {
        if (nodo == null) {
            return;
        }

        if (profundidadActual == profundidadDeseada) {
            nodosEnProfundidad.add(nodo);
            return;
        }

        for (Nodo hijo : nodo.getHijos()) {
            obtenerNodosEnProfundidadRecursivo(hijo, profundidadActual + 1, profundidadDeseada, nodosEnProfundidad);
        }
    }

    public Nodo buscarNodo(Nodo nodo, byte[][] dato) {
        if (nodo == null) {
            return null;
        }
        if (sonIguales(nodo.getDato(), dato)) {
            return nodo;
        }
        for (Nodo hijo : nodo.getHijos()) {
            Nodo resultado = buscarNodo(hijo, dato);
            if (resultado != null) {
                return resultado;
            }
        }
        return null;
    }

    private boolean sonIguales(byte[][] a1, byte[][] a2) {
        if (a1.length != a2.length || a1[0].length != a2[0].length) {
            return false;
        }
        for (int i = 0; i < a1.length; i++) {
            for (int j = 0; j < a1[i].length; j++) {
                if (a1[i][j] != a2[i][j]) {
                    return false;
                }
            }
        }
        return true;
    }

    public int altura(Nodo nodo) {
        if (nodo == null) {
            return 0;
        }
        int maxAltura = 0;
        for (Nodo hijo : nodo.getHijos()) {
            int alturaHijo = altura(hijo);
            if (alturaHijo > maxAltura) {
                maxAltura = alturaHijo;
            }
        }
        return maxAltura + 1;
    }
}