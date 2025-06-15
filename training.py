from typing import Generator 
from itertools import product 


#Exercice 1 

# def count_up_to(n):
#     for i in range(n+1):
#         yield i

# # for i in count_up_to(3):
# #     print(i)

#Ex2
# def even_numbers(n):
#     for i in range(n):
#         yield i*2
            

# for e in even_numbers(4):
#     print(e)

#Ex3 

# def gen_words(word: str, nombre:int):
#     for value in product(word, repeat=len(word)):
#         yield ''.join(value)

# for w in gen_words("ab", 2):
#     print(w)
