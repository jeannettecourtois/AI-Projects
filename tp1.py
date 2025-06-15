# Exercice 1

from typing import List, Dict, Generator 
from itertools import product #powerful tool that returns the Cartesian product of input iterables

def decomp_old(n: int, nb_bits: int) -> list[bool | int]:
    liste_booleen = []
    while n != 0:
        liste_booleen.append(n % 2)
        n = n // 2
    for i in range(len(liste_booleen)):
        if liste_booleen[i] == 1:
            liste_booleen[i] = True
        else:
            liste_booleen[i] = False
    if len(liste_booleen) != nb_bits:
        for i in range(nb_bits - len(liste_booleen)):
            liste_booleen.append(False)
    return liste_booleen


def decomp(n: int, nb_bits: int) -> list[bool]:
    liste_booleen = []
    for i in range(nb_bits):
        liste_booleen.append(n % 2 == 1)
        n //= 2
    return liste_booleen


# Exerice 2:


def interpretation(liste_cahine: list, liste_bool: list) -> dict:
    dictionnaire_interpretation = {}
    for i in range(len(liste_cahine)):
        dictionnaire_interpretation[liste_cahine[i]] = liste_bool[i]

    return dictionnaire_interpretation


# Exemple 3 :

def gen_interpretations(voc: list[str]) -> Generator[Dict[str, bool], None, None]:
    for values in product([False, True], repeat = len(voc)): 
        yield dict(zip(voc, values)) #conversion en dictionnaire clé/valeur 

# print(list(product([1, 2], [3, 4]))) -> [(1, 3), (1, 4), (2, 3), (2, 4)]
# print(dict(list(zip(['A', 'B', 'C'], (True, False, True))))) -> {'A': True, 'B': False, 'C': True}
# print(list(zip(['A', 'B', 'C'], (True, False, True)))) -> [('A', True), ('B', False), ('C', True)]
 

#Question 4 

def valuate(formula: str, interpretation: Dict[str, bool]) -> bool:
    return eval(formula, interpretation)

# eval(expression, globals, locals)
#Question 5 

def tabVerite(formula: str, vocabulaire: List[str]) -> Dict[tuple, bool]:
    dictVerite = {}
    for interpretation in gen_interpretations(vocabulaire):
        key = tuple(sorted(interpretation.items()))  # Transformer en tuple trié pour clé
        dictVerite[key] = valuate(formula, interpretation)
    return dictVerite
# interpretation.items()
# → dict_items([('A', True), ('C', False), ('B', True)])
# sorted([('A', True), ('C', False), ('B', True)])
# → [('A', True), ('B', True), ('C', False)]

#question 6 

def validite(formula: str, vocabulaire: List[str]):
    unTabVerite = tabVerite(formula, vocabulaire)
    lesTrue = 0
    lesFalse = 0
    for element in unTabVerite:
        if unTabVerite[element] == True:
            lesTrue +=1
        else:
            lesFalse += 1
    if lesTrue == 0:
        print("La formule est contradictoire")
    elif lesFalse == 0:
        print("La formule est valide.")
    else: 
        print("La formule est contingente")
            

#Question 7 

#corollaire 1 du Cours du théorème de la déduction 
#Si f2 est conséquence logique de f1, alors l'implication f1-> f2 est toujours vrai (une tautologie)
def is_cons(f1: str, f2: str, voc: List[str]) -> bool:
    implication = f"non({f1}) or ({f2})"
    return all(tabVerite(implication, voc).values())


def main():
    
    
    print(tabVerite("(A or B) and not(C)", ["A", "B", "C"]))
    


    # black nom.py
    # mypy nom.py
    # pylint nom.py
    
    
if __name__ == "__main__":
        main()
    # end main