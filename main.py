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

# Grid class -- represents the game grid
class Grid:
    def __init__(self, name='Default Grid', size=12):
        self.name = name
        self.size = size
        self.grid = [[Area(x, y) for y in range(size)] for x in range(size)]

    def get_area(self, x, y):
        return self.grid[x][y]

    def set_area(self, x, y, area):
        self.grid[x][y] = area

    def display(self):
        print(f"Displaying: '{self.name}':")
        print('  ' + ' '.join(str(i) for i in range(self.size)))
        for i, row in enumerate(self.grid):
            row_str = ''
            if i < 10:
                gap = ' '
            else:
                gap = ''
            row_str = str(i) + gap
            for j, area in enumerate(row):
                row_str += area.symbol
                if j > 9:
                    row_str += '  '
                else:
                    row_str += ' '
            print(row_str)
            i += 1

# Test zone

testGrid = Grid()
# Test the grid display
testGrid.display()
