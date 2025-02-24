package Puzzle8BFS;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Random;

public class Puzzle8 {

    public static void main(String[] args) {
        long inicio = System.nanoTime();

        Arbol posibilidades;
        byte[][] puzzle = new byte[3][3];
        byte[][] fin = {{1, 2, 3}, {4, 5, 6}, {7, 8, 0}};
        int cant = 0;

        init(puzzle);
        Random r = new Random();

        for (int i = 0; i < puzzle.length; i++) {
            for (int j = 0; j < puzzle.length; j++) {
                byte num = (byte) (r.nextInt(puzzle.length * puzzle[0].length));
                if (!existeNum(num, puzzle)) {
                    puzzle[i][j] = num;
                } else {
                    j--;
                }
            }
        }

        posibilidades = new Arbol(puzzle);

        System.out.println("=======ORIGINAL=======");
        for (int i = 0; i < puzzle.length; i++) {
            for (int j = 0; j < puzzle.length; j++) {
                System.out.printf("%-5s", puzzle[i][j]);
            }
            System.out.println();
        }
        System.out.println();

        List<byte[][]> lista = null;
        int profundidadDeseada = 0;
        List<Nodo> padres = posibilidades.obtenerNodosEnProfundidad(profundidadDeseada);
        boolean flag = false;
        int cont = -1;
        int nodosExplorados = 0; // Contador de nodos explorados
        Nodo nodoFinal = null; // Almacenará el nodo final (solución)

        while (!flag) {
            cont++;
            lista = sucesor(padres.get(cont).getDato());
            for (int i = 0; i < lista.size(); i++) {
                if (posibilidades.buscarNodo(posibilidades.getRaiz(), lista.get(i)) != null) {
                    continue;
                }
                cant++;
                posibilidades.agregarNodo(padres.get(cont), lista.get(i));
            }

            if (cont == padres.size() - 1) {
                profundidadDeseada++;
                padres = posibilidades.obtenerNodosEnProfundidad(profundidadDeseada);
                cont = -1;

                for (Nodo nodo : padres) {
                    nodosExplorados++; // Incrementar el contador de nodos explorados
                    if (nodo.compareTo(fin) == 0) {
                        nodoFinal = nodo; // Guardar el nodo final
                        flag = true;
                        break;
                    }
                }
            }
        }

        if (nodoFinal != null) {
            System.out.println("Solución encontrada:");
            mostrarCamino(nodoFinal); // Mostrar el camino desde la raíz hasta el nodo final
        } else {
            System.out.println("No se encontró solución.");
        }

        System.out.println("Número de movimientos: " + profundidadDeseada);
        System.out.println("Nodos explorados: " + nodosExplorados);
        System.out.println("Fin: " + cant);

        long fina = System.nanoTime();
        double tiempoEnSegundos = (fina - inicio) / 1_000_000_000.0;
        System.out.println("El programa tardó " + tiempoEnSegundos + " segundos en ejecutarse.");
    }

    public static void mostrarCamino(Nodo nodoFinal) {
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
        for (Nodo nodo : camino) {
            System.out.println("Paso " + nodo.getDato()[0][0] + ":");
            for (int i = 0; i < nodo.getDato().length; i++) {
                for (int j = 0; j < nodo.getDato()[i].length; j++) {
                    System.out.printf("%-5s", nodo.getDato()[i][j]);
                }
                System.out.println();
            }
            System.out.println();
        }
    }

    public static List<byte[][]> sucesor(byte[][] puzzle) {
        List<byte[][]> lista = new ArrayList<>();

        for (int i = 0; i < puzzle.length; i++) {
            for (int j = 0; j < puzzle.length; j++) {
                if ((i != 0 && i != puzzle.length - 1) && (j != 0 && j != puzzle[i].length - 1)) {
                    if (puzzle[i][j] == 0) {
                        lista.add(mover(puzzle, i - 1, j, i, j));
                        lista.add(mover(puzzle, i, j - 1, i, j));
                        lista.add(mover(puzzle, i + 1, j, i, j));
                        lista.add(mover(puzzle, i, j + 1, i, j));
                        return lista;
                    }
                } else if (i == 0 && j != 0 && j != puzzle[0].length - 1) {
                    if (puzzle[i][j] == 0) {
                        lista.add(mover(puzzle, i, j - 1, i, j));
                        lista.add(mover(puzzle, i + 1, j, i, j));
                        lista.add(mover(puzzle, i, j + 1, i, j));
                        return lista;
                    }
                } else if (j == 0 && i != 0 && i != puzzle.length - 1) {
                    if (puzzle[i][j] == 0) {
                        lista.add(mover(puzzle, i - 1, j, i, j));
                        lista.add(mover(puzzle, i, j + 1, i, j));
                        lista.add(mover(puzzle, i + 1, j, i, j));
                        return lista;
                    }
                } else if (i == puzzle.length - 1 && j != 0 && j != puzzle[0].length - 1) {
                    if (puzzle[i][j] == 0) {
                        lista.add(mover(puzzle, i, j - 1, i, j));
                        lista.add(mover(puzzle, i - 1, j, i, j));
                        lista.add(mover(puzzle, i, j + 1, i, j));
                        return lista;
                    }
                } else if (j == puzzle.length - 1 && i != 0 && i != puzzle.length - 1) {
                    if (puzzle[i][j] == 0) {
                        lista.add(mover(puzzle, i - 1, j, i, j));
                        lista.add(mover(puzzle, i, j - 1, i, j));
                        lista.add(mover(puzzle, i + 1, j, i, j));
                        return lista;
                    }
                } else if (i == 0 && j == 0) {
                    if (puzzle[i][j] == 0) {
                        lista.add(mover(puzzle, i, j + 1, i, j));
                        lista.add(mover(puzzle, i + 1, j, i, j));
                        return lista;
                    }
                } else if (i == puzzle.length - 1 && j == 0) {
                    if (puzzle[i][j] == 0) {
                        lista.add(mover(puzzle, i - 1, j, i, j));
                        lista.add(mover(puzzle, i, j + 1, i, j));
                        return lista;
                    }
                } else if (i == puzzle.length - 1 && j == puzzle[0].length - 1) {
                    if (puzzle[i][j] == 0) {
                        lista.add(mover(puzzle, i, j - 1, i, j));
                        lista.add(mover(puzzle, i - 1, j, i, j));
                        return lista;
                    }
                } else if (i == 0 && j == puzzle[0].length - 1) {
                    if (puzzle[i][j] == 0) {
                        lista.add(mover(puzzle, i, j - 1, i, j));
                        lista.add(mover(puzzle, i + 1, j, i, j));
                        return lista;
                    }
                }
            }
        }
        return lista;
    }

    public static boolean existeNum(byte num, byte[][] puzzle) {
        for (int i = 0; i < puzzle.length; i++) {
            for (int j = 0; j < puzzle.length; j++) {
                if (num == puzzle[i][j]) {
                    return true;
                }
            }
        }
        return false;
    }

    public static void init(byte[][] puzzle) {
        for (int i = 0; i < puzzle.length; i++) {
            for (int j = 0; j < puzzle.length; j++) {
                puzzle[i][j] = -1;
            }
        }
    }

    public static byte[][] mover(byte[][] puzzle, int pos1, int pos2, int pos3, int pos4) {
        byte[][] puzaux = new byte[puzzle.length][puzzle[0].length];
        fill(puzzle, puzaux);
        byte aux = puzaux[pos1][pos2];
        puzaux[pos1][pos2] = puzaux[pos3][pos4];
        puzaux[pos3][pos4] = aux;
        return puzaux;
    }

    public static void fill(byte[][] puzzle, byte[][] puzaux) {
        for (int i = 0; i < puzzle.length; i++) {
            for (int j = 0; j < puzzle[0].length; j++) {
                puzaux[i][j] = puzzle[i][j];
            }
        }
    }
}