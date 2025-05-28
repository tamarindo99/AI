import random
import time
from typing import List, Tuple, Set, Optional
import copy

class Nodo:
    def __init__(self, dato: List[List[int]], padre: 'Nodo' = None):
        self.padre = padre
        self.hijos: List['Nodo'] = []
        self.dato = dato

    def agregar_hijo(self, hijo: 'Nodo'):
        self.hijos.append(hijo)

    def eliminar_hijo(self, hijo: 'Nodo'):
        self.hijos.remove(hijo)

    def __eq__(self, other):
        if not isinstance(other, Nodo):
            return False
        return self.dato == other.dato

    def __hash__(self):
        return hash(tuple(tuple(fila) for fila in self.dato))

    def __str__(self):
        return f"Nodo(dato={self.dato})"

    def __repr__(self):
        return self.__str__()

class Arbol:
    def __init__(self, dato_raiz: List[List[int]] = None):
        if dato_raiz is None:
            self.raiz = None
        else:
            self.raiz = Nodo(dato_raiz)

    def esta_vacio(self) -> bool:
        return self.raiz is None

    def agregar_nodo(self, padre: Nodo, dato_hijo: List[List[int]]):
        if padre is None:
            raise ValueError("El nodo padre no puede ser nulo.")
        hijo = Nodo(dato_hijo, padre)
        padre.agregar_hijo(hijo)

    def buscar_nodo(self, nodo: Nodo, dato: List[List[int]]) -> Optional[Nodo]:
        if nodo is None:
            return None
        if self.son_iguales(nodo.dato, dato):
            return nodo
        for hijo in nodo.hijos:
            resultado = self.buscar_nodo(hijo, dato)
            if resultado is not None:
                return resultado
        return None

    @staticmethod
    def son_iguales(a1: List[List[int]], a2: List[List[int]]) -> bool:
        if len(a1) != len(a2) or len(a1[0]) != len(a2[0]):
            return False
        for i in range(len(a1)):
            for j in range(len(a1[0])):
                if a1[i][j] != a2[i][j]:
                    return False
        return True

def resolver_puzzle_dfs(puzzle: List[List[int]], fin: List[List[int]]) -> Optional[Nodo]:
    pila = []
    visitados = set()

    nodo_inicial = Nodo(puzzle)
    pila.append(nodo_inicial)

    while pila:
        actual = pila.pop()

        if actual.dato == fin:
            return actual  # Solución encontrada

        visitados.add(actual)

        for sucesor in generar_sucesores(actual.dato):
            nodo_sucesor = Nodo(sucesor, actual)

            if nodo_sucesor not in visitados:
                pila.append(nodo_sucesor)

    return None  # No se encontró solución

def mostrar_camino(nodo_final: Nodo):
    camino = []
    actual = nodo_final

    # Recorrer hacia atrás desde el nodo final hasta la raíz
    while actual is not None:
        camino.append(actual)
        actual = actual.padre

    # Invertir la lista para mostrar el camino desde la raíz hasta el nodo final
    camino.reverse()

    # Mostrar el camino
    for i, nodo in enumerate(camino):
        print(f"Paso {i}:")
        imprimir_puzzle(nodo.dato)

def generar_sucesores(puzzle: List[List[int]]) -> List[List[List[int]]]:
    sucesores = []
    posicion_vacia = encontrar_posicion_vacia(puzzle)

    movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Arriba, abajo, izquierda, derecha

    for movimiento in movimientos:
        nueva_fila = posicion_vacia[0] + movimiento[0]
        nueva_columna = posicion_vacia[1] + movimiento[1]

        if 0 <= nueva_fila < len(puzzle) and 0 <= nueva_columna < len(puzzle[0]):
            nuevo_puzzle = copiar_puzzle(puzzle)
            nuevo_puzzle[posicion_vacia[0]][posicion_vacia[1]] = nuevo_puzzle[nueva_fila][nueva_columna]
            nuevo_puzzle[nueva_fila][nueva_columna] = 0
            sucesores.append(nuevo_puzzle)

    return sucesores

def encontrar_posicion_vacia(puzzle: List[List[int]]) -> Tuple[int, int]:
    for i in range(len(puzzle)):
        for j in range(len(puzzle[0])):
            if puzzle[i][j] == 0:
                return (i, j)
    return (-1, -1)  # No debería ocurrir si el puzzle es válido

def copiar_puzzle(puzzle: List[List[int]]) -> List[List[int]]:
    return [fila.copy() for fila in puzzle]

def generar_puzzle_aleatorio() -> List[List[int]]:
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    random.shuffle(numeros)

    puzzle = [[0 for _ in range(3)] for _ in range(3)]
    index = 0
    for i in range(3):
        for j in range(3):
            puzzle[i][j] = numeros[index]
            index += 1

    return puzzle

def imprimir_puzzle(puzzle: List[List[int]]):
    for fila in puzzle:
        for valor in fila:
            print(f"{valor:<5}", end="")
        print()
    print()

def main():
    inicio = time.time()

    puzzle = generar_puzzle_aleatorio()
    fin = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    print("=======ORIGINAL=======")
    imprimir_puzzle(puzzle)

    solucion = resolver_puzzle_dfs(puzzle, fin)
    if solucion is not None:
        print("Solución encontrada:")
        mostrar_camino(solucion)
    else:
        print("No se encontró solución.")

    fina = time.time()
    tiempo_en_segundos = fina - inicio
    print(f"El programa tardó {tiempo_en_segundos} segundos en ejecutarse.")

if __name__ == "__main__":
    main()