package Puzzle8Heuristic;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Nodo implements Comparable<Nodo> {

    private Nodo padre;
    private List<Nodo> hijos;
    private byte[][] dato;
    private int g; // Cost from start to current node
    private int h; // Heuristic cost to goal

    public Nodo(byte[][] dato, int g, int h) {
        this.padre = null;
        this.hijos = new ArrayList<>();
        this.dato = dato;
        this.g = g;
        this.h = h;
    }

    public Nodo(Nodo padre, byte[][] dato, int g, int h) {
        this.padre = padre;
        this.hijos = new ArrayList<>();
        this.dato = dato;
        this.g = g;
        this.h = h;
    }

    public Nodo getPadre() {
        return padre;
    }

    public void setPadre(Nodo padre) {
        this.padre = padre;
    }

    public List<Nodo> getHijos() {
        return hijos;
    }

    public void agregarHijo(Nodo hijo) {
        hijos.add(hijo);
    }

    public void eliminarHijo(Nodo hijo) {
        hijos.remove(hijo);
    }

    public byte[][] getDato() {
        return dato;
    }

    public void setDato(byte[][] dato) {
        this.dato = dato;
    }

    public int getG() {
        return g;
    }

    public int getH() {
        return h;
    }

    public int getF() {
        return g + h;
    }

    @Override
    public String toString() {
        return "Nodo{" +
                "dato=" + Arrays.deepToString(dato) +
                ", g=" + g +
                ", h=" + h +
                '}';
    }

    @Override
    public int compareTo(Nodo o) {
        return Integer.compare(this.getF(), o.getF());
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;
        Nodo nodo = (Nodo) obj;
        return Arrays.deepEquals(dato, nodo.dato);
    }

    @Override
    public int hashCode() {
        return Arrays.deepHashCode(dato);
    }
}
