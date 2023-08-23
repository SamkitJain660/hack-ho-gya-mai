import random
import pypokedex
import time


player1 = []
player2 = []

for i in range(0,1):
    poke = input()
    if i <= 6:
        player1.append(poke.lower())
    else:
        player2.append(poke.lower())

for i in player1:
    pokemon = pypokedex.get(name=i.capitalize())
    try:
        pokemon.level = 100
        print(pokemon.level)
        
    except: print("nont")

#https://pypi.org/project/pypokedex/
