package Puzzle8BFS;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Nodo implements Comparable<byte[][]> {

    private Nodo padre;
    private List<Nodo> hijos;
    private byte[][] dato;

    public Nodo(byte[][] dato) {
        this.padre = null;
        this.hijos = new ArrayList<>();
        this.dato = dato;
    }

    public Nodo(Nodo padre, byte[][] dato) {
        this.padre = padre;
        this.hijos = new ArrayList<>();
        this.dato = dato;
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

    @Override
    public String toString() {
        return "Nodo{" +
                "dato=" + Arrays.deepToString(dato) +
                '}';
    }

    @Override
    public int compareTo(byte[][] o) {
        for (int i = 0; i < o.length; i++) {
            for (int j = 0; j < o[0].length; j++) {
                if (o[i][j] != this.dato[i][j]) {
                    return -1;
                }
            }
        }
        return 0;
    }
}