'''
This project is designed and coded by:
Amber Shifflett, 2025

Naval-Combat-System is a simple implementation of the classic game Battleship.
'''
# main.py

# imports
import random

# random number generator priming
random.seed()  # Seed the random number generator for randomness
random.random()  # Calls to burn some random numbers to ensure randomness in the first call
random.random()  # Calls to burn some random numbers to ensure randomness in the first call
random.random()  # Calls to burn some random numbers to ensure randomness in the first call

# Area class -- represents a single square in the game grid
class Area:
    def __init__(self, x, y, is_ship=False, is_hit=False, is_guessed=False, symbol='?'):
        self.x = x
        self.y = y
        self.is_ship = is_ship
        self.is_hit = is_hit
        self.is_guessed = is_guessed
        self.symbol = symbol
