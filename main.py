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

# Player class -- represents a player in the game
class Player:
    def __init__(self, name = 'Nameless'):
        self.ships = []
        self.name = name
        self.friendly_grid = Grid(name = self.name + ' Friendly Grid')
        self.enemy_grid = Grid(name = self.name + ' Enemy Grid')

# Test zone
user_input = ''
print('\n\n')
print('Welcome to Naval Combat System!')
# user_input = input('>>>>Enter a name for your player: <<<<\n')
user_input = 'Amber'  # For testing purposes, we can hardcode the name
user = Player(name=user_input)
print(f'Hello, {user.name}!\n')
user.enemy_grid.display()
print()
user.friendly_grid.display()
print()
print('Before we get started, let\'s set up your ships!')
print('You have 5 ships to place on your friendly grid. Coordinates are in the form of "x y" (x[space]y) where x is the column and y is the row.')
print('Let\'s start with the first ship.')
print('The first ship is 3 squares long. Provide the starting coordinates for the ship.')
try:
    ship_start = input('Enter coordinates (x y): ')
    x, y = map(int, ship_start.split())
    if 0 <= x < user.friendly_grid.size and 0 <= y < user.friendly_grid.size:
        print(f'Placing ship at ({x}, {y})')
        # Hold final changes until all ship spots are validated
        user.friendly_grid.get_area(y, x).symbol = 'S'
        # user.friendly_grid.set_area(y, x, Area(x, y, is_ship=True, symbol='S'))
    else:
        print('Coordinates out of bounds. Please try again.')
except ValueError:
    print('Invalid input. Please enter coordinates in the form "x y".')
print('Your friendly grid after placing the first part of the first ship:')
user.friendly_grid.display()