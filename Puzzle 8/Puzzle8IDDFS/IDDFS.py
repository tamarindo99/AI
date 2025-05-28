import random
import time
from typing import List, Tuple, Optional, Set
import sys

class Nodo:
    __slots__ = ['padre', 'hijos', 'dato', 'profundidad']
    
    def __init__(self, dato: List[List[int]], padre=None, profundidad=0):
        self.padre = padre
        self.hijos: List['Nodo'] = []
        self.dato = dato
        self.profundidad = profundidad

    def agregar_hijo(self, hijo: 'Nodo'):
        self.hijos.append(hijo)

    def __eq__(self, other: List[List[int]]) -> bool:
        return self.dato == other

    def __hash__(self):
        return hash(tuple(tuple(fila) for fila in self.dato))

    def __str__(self):
        return f"Nodo(dato={self.dato}, profundidad={self.profundidad})"

def resolver_puzzle_iddfs(puzzle: List[List[int]], fin: List[List[int]]) -> Optional[Nodo]:
    profundidad_maxima = 0
    visitados = set()
    
    while True:
        visitados.clear()
        solucion = buscar_en_profundidad_limitada(
            Nodo(puzzle, profundidad=0), 
            fin, 
            profundidad_maxima, 
            visitados
        )
        if solucion is not None:
            return solucion
        profundidad_maxima += 1
        if profundidad_maxima > 31:  # Límite teórico para 8-puzzle
            return None

def buscar_en_profundidad_limitada(
    nodo: Nodo, 
    fin: List[List[int]], 
    profundidad_maxima: int, 
    visitados: Set[Tuple[Tuple[int]]]
) -> Optional[Nodo]:
    if nodo.dato == fin:
        return nodo

    if nodo.profundidad >= profundidad_maxima:
        return None

    # Convertir a tupla de tuplas para hashing
    estado = tuple(tuple(fila) for fila in nodo.dato)
    if estado in visitados:
        return None
    visitados.add(estado)

    for sucesor in generar_sucesores(nodo.dato):
        nodo_sucesor = Nodo(sucesor, nodo, nodo.profundidad + 1)
        resultado = buscar_en_profundidad_limitada(
            nodo_sucesor, 
            fin, 
            profundidad_maxima, 
            visitados
        )
        if resultado is not None:
            return resultado

    return None

def mostrar_camino(nodo_final: Nodo):
    camino = []
    actual = nodo_final

    while actual is not None:
        camino.append(actual)
        actual = actual.padre

    camino.reverse()

    for i, paso in enumerate(camino):
        print(f"Paso {i} (Profundidad: {paso.profundidad}):")
        imprimir_puzzle(paso.dato)
    print(f"Longitud del camino: {len(camino)-1} movimientos")

def generar_sucesores(puzzle: List[List[int]]) -> List[List[List[int]]]:
    sucesores = []
    fila_vacia, columna_vacia = encontrar_posicion_vacia(puzzle)

    for df, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nueva_fila, nueva_columna = fila_vacia + df, columna_vacia + dc

        if 0 <= nueva_fila < 3 and 0 <= nueva_columna < 3:
            nuevo_puzzle = copiar_puzzle(puzzle)
            nuevo_puzzle[fila_vacia][columna_vacia] = nuevo_puzzle[nueva_fila][nueva_columna]
            nuevo_puzzle[nueva_fila][nueva_columna] = 0
            sucesores.append(nuevo_puzzle)

    return sucesores

def encontrar_posicion_vacia(puzzle: List[List[int]]) -> Tuple[int, int]:
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] == 0:
                return (i, j)
    return (-1, -1)

def copiar_puzzle(puzzle: List[List[int]]) -> List[List[int]]:
    return [fila.copy() for fila in puzzle]

def generar_puzzle_aleatorio() -> List[List[int]]:
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    
    while True:
        random.shuffle(numeros)
        puzzle = [numeros[i*3:(i+1)*3] for i in range(3)]
        if es_solucionable(puzzle):
            return puzzle

def es_solucionable(puzzle: List[List[int]]) -> bool:
    # Aplanar el puzzle y contar inversiones
    lista = [num for fila in puzzle for num in fila if num != 0]
    inversiones = 0
    
    for i in range(len(lista)):
        for j in range(i+1, len(lista)):
            if lista[i] > lista[j]:
                inversiones += 1
    
    # Encontrar la fila de la posición vacía (0)
    fila_vacia = 3 - [i for i in range(3) if 0 in puzzle[i]][0]
    
    return (inversiones % 2) == (fila_vacia % 2)

def imprimir_puzzle(puzzle: List[List[int]]):
    for fila in puzzle:
        print(" ".join(f"{num if num != 0 else ' ':>2}" for num in fila))
    print()

def main():
    # Configurar límite de recursión más alto
    sys.setrecursionlimit(10000)
    
    inicio = time.time()

    # Puzzle más fácil para prueba rápida
    # puzzle = [[1, 2, 3], [4, 5, 6], [7, 0, 8]]  # 1 movimiento
    puzzle = generar_puzzle_aleatorio()
    fin = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    print("======= ESTADO INICIAL =======")
    imprimir_puzzle(puzzle)

    print("Calculando solución...")
    solucion = resolver_puzzle_iddfs(puzzle, fin)
    
    if solucion is not None:
        print("\n======= SOLUCIÓN ENCONTRADA =======")
        mostrar_camino(solucion)
    else:
        print("No se encontró solución.")

    tiempo_ejecucion = time.time() - inicio
    print(f"Tiempo de ejecución: {tiempo_ejecucion:.2f} segundos")

if __name__ == "__main__":
    main()