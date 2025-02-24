package Puzzle8IDDFS;

import java.util.*;

public class Puzzle8 {

    public static void main(String[] args) {
        long inicio = System.nanoTime();

        byte[][] puzzle = generarPuzzleAleatorio();
        byte[][] fin = {{1, 2, 3}, {4, 5, 6}, {7, 8, 0}};

        System.out.println("=======ORIGINAL=======");
        imprimirPuzzle(puzzle);

        Nodo solucion = resolverPuzzleIDDFS(puzzle, fin);
        if (solucion != null) {
            System.out.println("Solución encontrada:");
            mostrarCamino(solucion);
        } else {
            System.out.println("No se encontró solución.");
        }

        long fina = System.nanoTime();
        double tiempoEnSegundos = (fina - inicio) / 1_000_000_000.0;
        System.out.println("El programa tardó " + tiempoEnSegundos + " segundos en ejecutarse.");
    }

    private static Nodo resolverPuzzleIDDFS(byte[][] puzzle, byte[][] fin) {
        int profundidadMaxima = 0;
        Nodo solucion = null;

        while (solucion == null) {
            solucion = buscarEnProfundidadLimitada(new Nodo(puzzle), fin, profundidadMaxima);
            profundidadMaxima++;
        }

        return solucion;
    }

    private static Nodo buscarEnProfundidadLimitada(Nodo nodo, byte[][] fin, int profundidadMaxima) {
        if (nodo.compareTo(fin) == 0) {
            return nodo; // Solución encontrada
        }

        if (profundidadMaxima <= 0) {
            return null; // Límite de profundidad alcanzado
        }

        for (byte[][] sucesor : generarSucesores(nodo.getDato())) {
            Nodo nodoSucesor = new Nodo(nodo, sucesor);
            Nodo resultado = buscarEnProfundidadLimitada(nodoSucesor, fin, profundidadMaxima - 1);
            if (resultado != null) {
                return resultado;
            }
        }

        return null; // No se encontró solución en esta profundidad
    }

    private static void mostrarCamino(Nodo nodoFinal) {
        List<Nodo> camino = new ArrayList<>();
        Nodo actual = nodoFinal;

        // Recorrer hacia atrás desde el nodo final hasta la raíz
        while (actual != null) {
            camino.add(actual);
            actual = actual.getPadre();
        }

        // Invertir la lista para mostrar el camino desde la raíz hasta el nodo final
        Collections.reverse(camino);

        // Mostrar el camino
        for (int i = 0; i < camino.size(); i++) {
            System.out.println("Paso " + i + ":");
            imprimirPuzzle(camino.get(i).getDato());
        }
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
}