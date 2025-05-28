import heapq
import random
import time
from copy import deepcopy
from typing import List, Tuple, Optional, Set, Dict

GOAL = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

class Node:
    def __init__(self, data: List[List[int]], g: int = 0, h: int = 0, parent: 'Node' = None):
        self.parent = parent
        self.children: List['Node'] = []
        self.data = data
        self.g = g  # Cost from start to current node
        self.h = h  # Heuristic cost to goal
    
    def __lt__(self, other: 'Node') -> bool:
        return (self.g + self.h) < (other.g + other.h)
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Node):
            return False
        return self.data == other.data
    
    def __hash__(self) -> int:
        return hash(tuple(tuple(row) for row in self.data))
    
    def __str__(self) -> str:
        return f"Node(data={self.data}, g={self.g}, h={self.h})"
    
    def get_f(self) -> int:
        return self.g + self.h
    
    def add_child(self, child: 'Node') -> None:
        self.children.append(child)

class Tree:
    def __init__(self, root_data: Optional[List[List[int]]] = None):
        self.root: Optional[Node] = None
        if root_data is not None:
            self.root = Node(root_data, 0, 0)
    
    def is_empty(self) -> bool:
        return self.root is None
    
    def add_node(self, parent: Node, child_data: List[List[int]], g: int, h: int) -> Node:
        if parent is None:
            raise ValueError("Parent node cannot be None")
        child = Node(child_data, g, h, parent)
        parent.add_child(child)
        return child

class Puzzle8:
    @staticmethod
    def main() -> None:
        start_time = time.time()
        
        puzzle = Puzzle8.generate_random_puzzle()
        print("=======ORIGINAL=======")
        Puzzle8.print_puzzle(puzzle)
        
        solution = Puzzle8.solve_puzzle(puzzle)
        if solution:
            print("Solution found:")
            Puzzle8.print_path(solution)
            print(f"Number of moves: {solution.g}")
        else:
            print("No solution found.")
        
        end_time = time.time()
        print(f"Program took {end_time - start_time:.4f} seconds to execute.")
    
    @staticmethod
    def solve_puzzle(puzzle: List[List[int]]) -> Optional[Node]:
        open_list: List[Node] = []
        closed_set: Set[Node] = set()
        nodes_explored = 0
        
        initial_node = Node(puzzle, 0, Puzzle8.calculate_heuristic(puzzle))
        heapq.heappush(open_list, initial_node)
        
        tree = Tree(puzzle)
        tree.root = initial_node
        
        while open_list:
            current_node = heapq.heappop(open_list)
            nodes_explored += 1
            
            if current_node.data == GOAL:
                print(f"Nodes explored: {nodes_explored}")
                return current_node
            
            closed_set.add(current_node)
            
            for successor in Puzzle8.generate_successors(current_node.data):
                successor_node = Node(
                    successor,
                    current_node.g + 1,
                    Puzzle8.calculate_heuristic(successor),
                    current_node
                )
                
                if successor_node not in closed_set:
                    heapq.heappush(open_list, successor_node)
                    tree.add_node(current_node, successor, successor_node.g, successor_node.h)
        
        print(f"Nodes explored: {nodes_explored}")
        return None
    
    @staticmethod
    def calculate_heuristic(puzzle: List[List[int]]) -> int:
        heuristic = 0
        for i in range(3):
            for j in range(3):
                if puzzle[i][j] != GOAL[i][j] and puzzle[i][j] != 0:
                    heuristic += 1
        return heuristic
    
    @staticmethod
    def generate_successors(puzzle: List[List[int]]) -> List[List[List[int]]]:
        successors = []
        empty_pos = Puzzle8.find_empty_position(puzzle)
        
        movements = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, down, left, right
        
        for move in movements:
            new_row = empty_pos[0] + move[0]
            new_col = empty_pos[1] + move[1]
            
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_puzzle = deepcopy(puzzle)
                new_puzzle[empty_pos[0]][empty_pos[1]] = new_puzzle[new_row][new_col]
                new_puzzle[new_row][new_col] = 0
                successors.append(new_puzzle)
        
        return successors
    
    @staticmethod
    def find_empty_position(puzzle: List[List[int]]) -> Tuple[int, int]:
        for i in range(3):
            for j in range(3):
                if puzzle[i][j] == 0:
                    return (i, j)
        raise ValueError("Empty position (0) not found in puzzle")
    
    @staticmethod
    def generate_random_puzzle() -> List[List[int]]:
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 0]
        random.shuffle(numbers)
        
        puzzle = []
        for i in range(3):
            row = []
            for j in range(3):
                row.append(numbers[i * 3 + j])
            puzzle.append(row)
        
        return puzzle
    
    @staticmethod
    def print_puzzle(puzzle: List[List[int]]) -> None:
        for row in puzzle:
            print(" ".join(f"{val:<3}" for val in row))
        print()
    
    @staticmethod
    def print_path(node: Node) -> None:
        path = []
        while node:
            path.append(node)
            node = node.parent
        path.reverse()
        
        for n in path:
            Puzzle8.print_puzzle(n.data)

if __name__ == "__main__":
    Puzzle8.main()