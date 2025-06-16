import random 
import itertools 
import networkx as nx 
import matplotlib.pyplot as plt 


#TP2 
# Exercice 2 : licorne.cnf 

# c 
# c Problème de la licorne 
# c 
# p cnf 5 6 
# -1 -2 0
# 1 4 0
# 1 2 0
# -4 5 0
# 2 5 0
# -5 3 0

#sortie de commande 
# c solving .\licorne.cnf
# s SATISFIABLE
# v -1 2 3 4 5 0

#Pour les autres questions on raisonne avec le théorème de déduction

# Peut-on déduire que la licorne a une corne ? Oui
# s UNSATISFIABLE (en rajoutant -5)
# Qu’elle n’a pas de corne ? Non 
# s SATISFIABLE (en rajoutant 5)
# v -1 2 3 4 5 0
#  Peut-on déduire qu’elle est mythique ? Qu’elle n’est pas mythique ? On ne peut pas conclure
#Pour 1 et -1 on obitnet satisfiable 
# s SATISFIABLE
# v -1 2 3 4 5 0
# c solving .\licorne.cnf
# s SATISFIABLE
# v 1 -2 3 -4 5 0



#Exercice 3 

def couleur_validee(graph, coloring):
    for u, v in graph.edges():
        if coloring[u] == coloring[v]:
            return False
    return True 

def greedy_coloring(graph):
    coloring = {}
    for node in graph.nodes():
        adjacent_colors = {coloring.get(neighbor) for neighbor in graph.neighbors(node)}
        coloring[node] = next(color for color in itertools.count() if color not in adjacent_colors)
    return coloring 




def main():
    n_nodes = 10
    G = nx.Graph()
    G.add_nodes_from(range(n_nodes))
    for i in range(n_nodes):
        for j in range(i+1, n_nodes):
            if random.random() < 0.1:
                G.add_edge(i, j)
    
    coloring_result = greedy_coloring(G)
    print('Coloring: ', coloring_result)
    print('Valid: ', couleur_validee(G, coloring_result))
    print('K: ', len(set(coloring_result.values())))
    
    color_map = [coloring_result[node] for node in G.nodes()]
    nx.draw(G, node_color = color_map, with_labels = True, font_weight = 'bold')
    plt.show()
    
    #https://www.youtube.com/watch?v=AyrrZ4PCyws&t=670s


if __name__ == "__main__":
        main()
    
    