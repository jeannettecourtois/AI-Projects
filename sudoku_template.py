"""
[IA02] TP SAT/Sudoku template python
author:  Sylvain Lagrue
version: 1.1.1
licence: WTFPL <https://www.wtfpl.net/txt/copying/>
"""

import subprocess
from model import model
from itertools import combinations

# alias de types
Grid = list[list[int]]
PropositionnalVariable = int
Literal = int
Clause = list[Literal]
ClauseBase = list[Clause]
Model = list[Literal]

example: Grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]


example2: Grid = [
    [0, 0, 0, 0, 2, 7, 5, 8, 0],
    [1, 0, 0, 0, 0, 0, 0, 4, 6],
    [0, 0, 0, 0, 0, 9, 0, 0, 0],
    [0, 0, 3, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 5, 0, 2, 0],
    [0, 0, 0, 8, 1, 0, 0, 0, 0],
    [4, 0, 6, 3, 0, 1, 0, 0, 9],
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [7, 2, 0, 0, 0, 0, 3, 1, 0],
]


empty_grid: Grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]

#### fonctions fournies


def write_dimacs_file(dimacs: str, filename: str):
    with open(filename, "w", newline="") as cnf:
        cnf.write(dimacs)


def exec_gophersat(
    filename: str, cmd: str = "gophersat", encoding: str = "utf8"
) -> tuple[bool, list[int]]:
    result = subprocess.run(
        [cmd, filename], capture_output=True, check=True, encoding=encoding
    )
    string = str(result.stdout)
    lines = string.splitlines()

    if lines[1] != "s SATISFIABLE":
        return False, []

    model = lines[2][2:-2].split(" ")

    return True, [int(x) for x in model]

#Premières questions 

#Question 1 
#On a 9*9*9=729 variables 
#at least 

#### fonction principale
def cell_to_variable(i: int, j: int, val: int) -> PropositionnalVariable:
    return 81 * i + 9 * j + val
    
def variable_to_cell(var: int) -> tuple[int, int, int]:
    var -= 1
    i = var // 81
    j = (var % 81) // 9
    val = (var % 9) + 1
    return i, j, val

def at_least_one(vars: list[int]) -> list[int]:
    return vars
from itertools import combinations

def unique(vars: list[int]) -> list[list[int]]:
    base = [at_least_one(vars)]
    for (x, y) in combinations(vars, 2):
        base.append([-x, -y])
    return base
def create_cell_constraints() -> list[list[int]]:
    clauses = []
    for i in range(9):
        for j in range(9):
            vars = [cell_to_variable(i, j, val) for val in range(1, 10)]
            clauses += unique(vars)
    return clauses
def create_line_constraints() -> list[list[int]]:
    clauses = []
    for i in range(9):
        for val in range(1, 10):
            vars = [cell_to_variable(i, j, val) for j in range(9)]
            clauses += unique(vars)
    return clauses

def create_column_constraints() -> list[list[int]]:
    clauses = []
    for j in range(9):
        for val in range(1, 10):
            vars = [cell_to_variable(i, j, val) for i in range(9)]
            clauses += unique(vars)
    return clauses

def create_box_constraints() -> list[list[int]]:
    clauses = []
    for bi in range(3):
        for bj in range(3):
            for val in range(1, 10):
                vars = []
                for i in range(3):
                    for j in range(3):
                        vars.append(cell_to_variable(3 * bi + i, 3 * bj + j, val))
                clauses += unique(vars)
    return clauses
def create_value_constraints(grid: Grid) -> list[list[int]]:
    clauses = []
    for i in range(9):
        for j in range(9):
            val = grid[i][j]
            if val != 0:
                clauses.append([cell_to_variable(i, j, val)])
    return clauses

def generate_problem(grid: Grid) -> ClauseBase:
    return (
        create_cell_constraints()
        + create_line_constraints()
        + create_column_constraints()
        + create_box_constraints()
        + create_value_constraints(grid)
    )
def clauses_to_dimacs(clauses: ClauseBase, nb_vars: int) -> str:
    dimacs = f"p cnf {nb_vars} {len(clauses)}\n"
    for clause in clauses:
        dimacs += " ".join(map(str, clause)) + " 0\n"
    return dimacs

def model_to_grid(model: Model, nb_vals: int = 9) -> Grid:
    grid = [[0 for _ in range(nb_vals)] for _ in range(nb_vals)]
    for literal in model:
        if literal > 0:
            i, j, val = variable_to_cell(literal)
            grid[i][j] = val
    return grid
  
def main():
    pass


if __name__ == "__main__":
    print(cell_to_variable(1, 3, 4))
    print(at_least_one([1, 3, 5]))
    main()
