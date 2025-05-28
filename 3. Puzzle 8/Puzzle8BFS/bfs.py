import copy
import random
import time
from typing import List, Optional, Tuple

class Nodo:
    def __init__(self, dato: List[List[int]], padre: Optional['Nodo'] = None):
        self.padre = padre
        self.hijos: List[Nodo] = []
        self.dato = copy.deepcopy(dato)

    def agregar_hijo(self, hijo: 'Nodo'):
        self.hijos.append(hijo)

    def eliminar_hijo(self, hijo: 'Nodo'):
        self.hijos.remove(hijo)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Nodo):
            return False
        return self.dato == other.dato

    def __str__(self) -> str:
        return f"Nodo(dato={self.dato})"

    def __repr__(self) -> str:
        return self.__str__()

class Arbol:
    def __init__(self, dato_raiz: Optional[List[List[int]]] = None):
        self.raiz: Optional[Nodo] = None
        if dato_raiz is not None:
            self.raiz = Nodo(dato_raiz)

    def esta_vacio(self) -> bool:
        return self.raiz is None

    def agregar_nodo(self, padre: Nodo, dato_hijo: List[List[int]]) -> Nodo:
        if padre is None:
            raise ValueError("El nodo padre no puede ser nulo.")
        hijo = Nodo(dato_hijo, padre)
        padre.agregar_hijo(hijo)
        return hijo

    def obtener_nodos_en_profundidad(self, profundidad_deseada: int) -> List[Nodo]:
        nodos_en_profundidad: List[Nodo] = []
        self._obtener_nodos_en_profundidad_recursivo(self.raiz, 0, profundidad_deseada, nodos_en_profundidad)
        return nodos_en_profundidad

    def _obtener_nodos_en_profundidad_recursivo(self, nodo: Optional[Nodo], profundidad_actual: int,
                                              profundidad_deseada: int, nodos_en_profundidad: List[Nodo]):
        if nodo is None:
            return

        if profundidad_actual == profundidad_deseada:
            nodos_en_profundidad.append(nodo)
            return

        for hijo in nodo.hijos:
            self._obtener_nodos_en_profundidad_recursivo(hijo, profundidad_actual + 1, 
                                                       profundidad_deseada, nodos_en_profundidad)

    def buscar_nodo(self, nodo: Optional[Nodo], dato: List[List[int]]) -> Optional[Nodo]:
        if nodo is None:
            return None
        if son_iguales(nodo.dato, dato):
            return nodo
        for hijo in nodo.hijos:
            resultado = self.buscar_nodo(hijo, dato)
            if resultado is not None:
                return resultado
        return None

    def altura(self, nodo: Optional[Nodo]) -> int:
        if nodo is None:
            return 0
        max_altura = 0
        for hijo in nodo.hijos:
            altura_hijo = self.altura(hijo)
            if altura_hijo > max_altura:
                max_altura = altura_hijo
        return max_altura + 1

def son_iguales(a1: List[List[int]], a2: List[List[int]]) -> bool:
    if len(a1) != len(a2) or len(a1[0]) != len(a2[0]):
        return False
    for i in range(len(a1)):
        for j in range(len(a1[i])):
            if a1[i][j] != a2[i][j]:
                return False
    return True

def init(puzzle: List[List[int]]):
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            puzzle[i][j] = -1

def existe_num(num: int, puzzle: List[List[int]]) -> bool:
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            if num == puzzle[i][j]:
                return True
    return False

def mover(puzzle: List[List[int]], pos1: int, pos2: int, pos3: int, pos4: int) -> List[List[int]]:
    puzaux = copy.deepcopy(puzzle)
    aux = puzaux[pos1][pos2]
    puzaux[pos1][pos2] = puzaux[pos3][pos4]
    puzaux[pos3][pos4] = aux
    return puzaux

def sucesor(puzzle: List[List[int]]) -> List[List[List[int]]]:
    lista: List[List[List[int]]] = []

    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            if (i != 0 and i != len(puzzle) - 1) and (j != 0 and j != len(puzzle[i]) - 1):
                if puzzle[i][j] == 0:
                    lista.append(mover(puzzle, i - 1, j, i, j))
                    lista.append(mover(puzzle, i, j - 1, i, j))
                    lista.append(mover(puzzle, i + 1, j, i, j))
                    lista.append(mover(puzzle, i, j + 1, i, j))
                    return lista
            elif i == 0 and j != 0 and j != len(puzzle[0]) - 1:
                if puzzle[i][j] == 0:
                    lista.append(mover(puzzle, i, j - 1, i, j))
                    lista.append(mover(puzzle, i + 1, j, i, j))
                    lista.append(mover(puzzle, i, j + 1, i, j))
                    return lista
            elif j == 0 and i != 0 and i != len(puzzle) - 1:
                if puzzle[i][j] == 0:
                    lista.append(mover(puzzle, i - 1, j, i, j))
                    lista.append(mover(puzzle, i, j + 1, i, j))
                    lista.append(mover(puzzle, i + 1, j, i, j))
                    return lista
            elif i == len(puzzle) - 1 and j != 0 and j != len(puzzle[0]) - 1:
                if puzzle[i][j] == 0:
                    lista.append(mover(puzzle, i, j - 1, i, j))
                    lista.append(mover(puzzle, i - 1, j, i, j))
                    lista.append(mover(puzzle, i, j + 1, i, j))
                    return lista
            elif j == len(puzzle) - 1 and i != 0 and i != len(puzzle) - 1:
                if puzzle[i][j] == 0:
                    lista.append(mover(puzzle, i - 1, j, i, j))
                    lista.append(mover(puzzle, i, j - 1, i, j))
                    lista.append(mover(puzzle, i + 1, j, i, j))
                    return lista
            elif i == 0 and j == 0:
                if puzzle[i][j] == 0:
                    lista.append(mover(puzzle, i, j + 1, i, j))
                    lista.append(mover(puzzle, i + 1, j, i, j))
                    return lista
            elif i == len(puzzle) - 1 and j == 0:
                if puzzle[i][j] == 0:
                    lista.append(mover(puzzle, i - 1, j, i, j))
                    lista.append(mover(puzzle, i, j + 1, i, j))
                    return lista
            elif i == len(puzzle) - 1 and j == len(puzzle[0]) - 1:
                if puzzle[i][j] == 0:
                    lista.append(mover(puzzle, i, j - 1, i, j))
                    lista.append(mover(puzzle, i - 1, j, i, j))
                    return lista
            elif i == 0 and j == len(puzzle[0]) - 1:
                if puzzle[i][j] == 0:
                    lista.append(mover(puzzle, i, j - 1, i, j))
                    lista.append(mover(puzzle, i + 1, j, i, j))
                    return lista
    return lista

def mostrar_camino(nodo_final: Nodo):
    camino: List[Nodo] = []
    actual = nodo_final

    # Recorrer hacia atrás desde el nodo final hasta la raíz
    while actual is not None:
        camino.append(actual)
        actual = actual.padre

    # Invertir la lista para mostrar el camino desde la raíz hasta el nodo final
    camino.reverse()

    # Mostrar el camino
    for paso, nodo in enumerate(camino):
        print(f"Paso {paso}:")
        for fila in nodo.dato:
            print(" ".join(f"{num:2}" for num in fila))
        print()

def main():
    inicio = time.time()

    puzzle = [[-1 for _ in range(3)] for _ in range(3)]
    fin = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    cant = 0

    # Generar puzzle aleatorio
    numeros = list(range(9))
    random.shuffle(numeros)
    for i in range(3):
        for j in range(3):
            puzzle[i][j] = numeros[i * 3 + j]

    posibilidades = Arbol(puzzle)

    print("=======ORIGINAL=======")
    for fila in puzzle:
        print(" ".join(f"{num:2}" for num in fila))
    print()

    lista: List[List[List[int]]] = []
    profundidad_deseada = 0
    padres = posibilidades.obtener_nodos_en_profundidad(profundidad_deseada)
    flag = False
    cont = -1
    nodos_explorados = 0
    nodo_final = None

    while not flag and padres:
        cont += 1
        lista = sucesor(padres[cont].dato)
        for movimiento in lista:
            if posibilidades.buscar_nodo(posibilidades.raiz, movimiento) is not None:
                continue
            cant += 1
            posibilidades.agregar_nodo(padres[cont], movimiento)

        if cont == len(padres) - 1:
            profundidad_deseada += 1
            padres = posibilidades.obtener_nodos_en_profundidad(profundidad_deseada)
            cont = -1

            for nodo in padres:
                nodos_explorados += 1
                if son_iguales(nodo.dato, fin):
                    nodo_final = nodo
                    flag = True
                    break

    if nodo_final is not None:
        print("Solución encontrada:")
        mostrar_camino(nodo_final)
    else:
        print("No se encontró solución.")

    print(f"Número de movimientos: {profundidad_deseada}")
    print(f"Nodos explorados: {nodos_explorados}")
    print(f"Fin: {cant}")

    fina = time.time()
    tiempo_en_segundos = fina - inicio
    print(f"El programa tardó {tiempo_en_segundos:.2f} segundos en ejecutarse.")

if __name__ == "__main__":
    main()