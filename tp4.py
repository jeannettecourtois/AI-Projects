import math as mt
from typing import Callable
import random
import numpy as np 

# Quelques structures de données

Grid = tuple[tuple[int, ...], ...]
State = Grid
Action = tuple[int, int]
Player = int
Score = float

# Quelques constantes
DRAW = 0
EMPTY = 0
X = 1
O = 2

#grilles prédéfinies 

EMPTY_GRID: Grid = ((0, 0, 0), (0, 0, 0), (0, 0, 0))
GRID_0: Grid = EMPTY_GRID
GRID_1: Grid = ((0, 0, 0), (0, X, O), (0, 0, 0))
# (0, 0, 0),
# (0, X, O),
# (0, 0, 0))

GRID_2: Grid = ((O, 0, X), (X, X, O), (O, X, 0))
#((O, 0, X),
# (X, X, O),
# (O, X, 0)

GRID_3: Grid = ((O, 0, X), (0, X, O), (O, X, 0))
#((O, 0, X),
# (0, X, O),
# (O, X, 0))

GRID_4: Grid = ((0, 0, 0), (X, X, O), (0, 0, 0))
#((0, 0, 0),
# (X, X, O),
# (0, 0, 0))


# fonctions préliminaires  préliminaires


def grid_tuple_to_grid_list(grid: Grid) -> list[list[int]]:
    return [list(row) for row in grid]


def grid_list_to_grid_tuple(grid: list[list[int]]) -> Grid:
    return tuple(tuple(row) for row in grid)


# fonction legals
def legals(grid: State) -> list[Action]:
    maGrid = grid_tuple_to_grid_list(grid)
    liste_actions = []
    for i in range(len(maGrid)):
        for j in range(len(maGrid[0])):
            if maGrid[i][j] == EMPTY:
                liste_actions.append((i, j))
    return liste_actions


# fonction line
def line(grid: State, player: Player) -> bool:
    maGrid = grid_tuple_to_grid_list(grid)
    if line_ligne(maGrid, player):
        return True
    elif line_colonne(maGrid, player):
        return True
    elif line_diagonale(maGrid, player):
        return True
    else:
        return False


def line_ligne(grid: list, player: Player) -> bool:
    for element in grid:
        if all([row == player for row in element]):
            return True
    return False


def line_colonne(grid: list, player: Player) -> bool:
    for j in range(len(grid[0])):
        if all([grid[i][j] == player for i in range(len(grid))]):
            return True
    return False


def line_diagonale(grid: list, player: Player) -> bool:
    # il y a deux diagonales
    if all([grid[i][i] == player for i in range(len(grid))]):
        return True
    elif all([grid[i][len(grid) - 1 - i] == player for i in range(len(grid))]):
        return True
    else:
        return False


# Fonction finale: ça renvoie si un joueur a gagné


def final(grid: State) -> Score:
    # maGrid = grid_tuple_to_grid_list(grid)
    if legals(grid) == []:
        return True
    elif line(grid, X):
        return True
    elif line(grid, O):
        return True
    else:
        return False


#Fonction score: fonction qui retourne le score du jeu -> celui qui a gagné

def score(grid:State) -> Score: 
    if final(grid) and line(grid, X):
        return 1 
    elif final(grid) and line(grid, O):
        return -1
    else:
        return 0


#affichage en console avec la fonction 
def pprint(grid: State):
    maGrid = grid_tuple_to_grid_list(grid)
    for i in range(len(maGrid)):
        print('\n')
        for j in range(len(maGrid[0])):
            if maGrid[i][j] == EMPTY: 
                print('.', end=' ')
            elif maGrid[i][j] == O:
                print('O', end=' ')
            elif maGrid[i][j] == X:
                print('X', end=' ')
    print('\n')
    return 


def play(grid: State, player: Player, action: Action)->State:
    maGrid = grid_tuple_to_grid_list(grid)
    maGrid[action[0]][action[1]] = player
    return grid_list_to_grid_tuple(maGrid)



#Ajout de premiers joueurs et boucle de jeu 
#stategy est une fonction qui renvoie une action à partir 
# d'un état et d'un joueur 
Strategy = Callable[[State, Player], Action]

def stategy_random(grid: State, player: Player) -> Action:
    return random.choice(legals(grid))


def strategy_brain(grid: State, player: Player) -> Action:
    print("à vous de jouer: ", end="")
    s = input()
    print()
    t = ast.literal_eval(s)

    return t



#fonction intermédiaire
def tour_de_jeu(grid: State, player: Player, strategy: Callable[[State, Player], Action]) -> State:
    return play(grid, player, strategy(grid, player)) #ça renvoie un état 



def tictactoe(strategy_X: Strategy, strategy_O: Strategy, debug: bool = False) -> Score:
    #tant que le jeu n'est pas fini
    grid = EMPTY_GRID
    player = X
    while (not(final(grid))):
        strategy = strategy_X if player == X else strategy_O
        grid = tour_de_jeu(grid, player, strategy)
        player = O if player == X else X
    return score(grid)


#fonction tictactoe 

# def minmax(grid: State, player: Player) -> Score:
#     if final(grid):
#         return score(grid)
#     if player == X:
#         bestValue = -1
#         #on fait juste une partie du code 
#         for el

        
        




#minmax de base 

# def minmax(grid: State, player: Player) -> Score:
#     if final(grid):
#         return score(grid)
    



def main():
    grid1 = ((O, X, EMPTY), (O, EMPTY, O), (O, X, O))
    #pprint(grid1)
    
    #pprint(play(grid1, X, (0, 0)))

    print(stategy_random(grid1, X))

    #strategy_brain(grid1, X)
    


if __name__ == "__main__":
    main()