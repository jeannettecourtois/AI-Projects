


#TP2 

#Exercice 3 

#Nombre de sommets:
couleurs = ["V", "R", "B"]
sommets = ["A", "B", "C"]

clauses = [['A_R', '-B_V', '-C_B'], [] ]


#construction de toutes les possbilités 
voc = {}
count = 0
for sommet in sommets: 
    for couleur in couleurs: 
        key = f"{sommet}_{couleur}"
        voc[key] = count
        count += 1

# graphe de couleurs 