package Puzzle8Heuristic;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashSet;
import java.util.List;
import java.util.PriorityQueue;
import java.util.Set;

public class Puzzle8 {

    private static final byte[][] GOAL = {{1, 2, 3}, {4, 5, 6}, {7, 8, 0}};

    public static void main(String[] args) {
        long inicio = System.nanoTime();

        byte[][] puzzle = generarPuzzleAleatorio();
        System.out.println("=======ORIGINAL=======");
        imprimirPuzzle(puzzle);

        Nodo solucion = resolverPuzzle(puzzle);
        if (solucion != null) {
            System.out.println("Solución encontrada:");
            imprimirCamino(solucion);
            System.out.println("Número de movimientos: " + solucion.getG());
        } else {
            System.out.println("No se encontró solución.");
        }

        long fin = System.nanoTime();
        double tiempoEnSegundos = (fin - inicio) / 1_000_000_000.0;
        System.out.println("El programa tardó " + tiempoEnSegundos + " segundos en ejecutarse.");
    }

    private static Nodo resolverPuzzle(byte[][] puzzle) {
        PriorityQueue<Nodo> colaAbierta = new PriorityQueue<>();
        Set<Nodo> cerrados = new HashSet<>();

        Nodo nodoInicial = new Nodo(puzzle, 0, calcularHeuristica(puzzle));
        colaAbierta.add(nodoInicial);

        Arbol arbol = new Arbol(puzzle);
        arbol.setRaiz(nodoInicial);

        int nodosExplorados = 0; // Contador de nodos explorados

        while (!colaAbierta.isEmpty()) {
            Nodo actual = colaAbierta.poll();
            nodosExplorados++; // Incrementar el contador de nodos explorados

            if (Arrays.deepEquals(actual.getDato(), GOAL)) {
                System.out.println("Nodos explorados: " + nodosExplorados);
                return actual;
            }

            cerrados.add(actual);

            for (byte[][] sucesor : generarSucesores(actual.getDato())) {
                Nodo nodoSucesor = new Nodo(actual, sucesor, actual.getG() + 1, calcularHeuristica(sucesor));

                if (!cerrados.contains(nodoSucesor)) {
                    colaAbierta.add(nodoSucesor);
                    arbol.agregarNodo(actual, sucesor, nodoSucesor.getG(), nodoSucesor.getH());
                }
            }
        }

        System.out.println("Nodos explorados: " + nodosExplorados);
        return null;
    }

    private static int calcularHeuristica(byte[][] puzzle) {
        int heuristica = 0;
        for (int i = 0; i < puzzle.length; i++) {
            for (int j = 0; j < puzzle[i].length; j++) {
                if (puzzle[i][j] != GOAL[i][j] && puzzle[i][j] != 0) {
                    heuristica++;
                }
            }
        }
        return heuristica;
    }

    private static List<byte[][]> generarSucesores(byte[][] puzzle) {
        List<byte[][]> sucesores = new ArrayList<>();
        int[] posicionVacia = encontrarPosicionVacia(puzzle);

        int[][] movimientos = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}}; // Arriba, abajo, izquierda, derecha

        for (int[] movimiento : movimientos) {
            int nuevaFila = posicionVacia[0] + movimiento[0];
            int nuevaColumna = posicionVacia[1] + movimiento[1];

            if (nuevaFila >= 0 && nuevaFila < puzzle.length && nuevaColumna >= 0 && nuevaColumna < puzzle[0].length) {
                byte[][] nuevoPuzzle = copiarPuzzle(puzzle);
                nuevoPuzzle[posicionVacia[0]][posicionVacia[1]] = nuevoPuzzle[nuevaFila][nuevaColumna];
                nuevoPuzzle[nuevaFila][nuevaColumna] = 0;
                sucesores.add(nuevoPuzzle);
            }
        }

        return sucesores;
    }

    private static int[] encontrarPosicionVacia(byte[][] puzzle) {
        for (int i = 0; i < puzzle.length; i++) {
            for (int j = 0; j < puzzle[i].length; j++) {
                if (puzzle[i][j] == 0) {
                    return new int[]{i, j};
                }
            }
        }
        return null;
    }

    private static byte[][] copiarPuzzle(byte[][] puzzle) {
        byte[][] copia = new byte[puzzle.length][puzzle[0].length];
        for (int i = 0; i < puzzle.length; i++) {
            System.arraycopy(puzzle[i], 0, copia[i], 0, puzzle[i].length);
        }
        return copia;
    }

    private static byte[][] generarPuzzleAleatorio() {
        byte[][] puzzle = new byte[3][3];
        List<Byte> numeros = new ArrayList<>(Arrays.asList((byte) 1, (byte) 2, (byte) 3, (byte) 4, (byte) 5, (byte) 6, (byte) 7, (byte) 8, (byte) 0));
        Collections.shuffle(numeros);

        int index = 0;
        for (int i = 0; i < puzzle.length; i++) {
            for (int j = 0; j < puzzle[i].length; j++) {
                puzzle[i][j] = numeros.get(index++);
            }
        }

        return puzzle;
    }

    private static void imprimirPuzzle(byte[][] puzzle) {
        for (byte[] fila : puzzle) {
            for (byte valor : fila) {
                System.out.printf("%-5s", valor);
            }
            System.out.println();
        }
        System.out.println();
    }

    private static void imprimirCamino(Nodo nodo) {
        List<Nodo> camino = new ArrayList<>();
        while (nodo != null) {
            camino.add(nodo);
            nodo = nodo.getPadre();
        }
        Collections.reverse(camino);

        for (Nodo n : camino) {
            imprimirPuzzle(n.getDato());
        }
    }
}