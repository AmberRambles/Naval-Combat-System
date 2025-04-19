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
    def debugPrint(self):
        print('This Area contains:')
        print(f'x: {self.x}')
        print(f'y: {self.y}')
        print(f'is_ship: {self.is_ship}')
        print(f'is_hit: {self.is_hit}')
        print(f'is_guessed: {self.is_guessed}')
        print(f'symbol: {self.symbol}')
        print()

# Grid class -- represents the game grid
class Grid:
    def __init__(self, name='Default Grid', size=12):
        self.name = name
        self.size = size
        self.grid = [[Area(x, y) for x in range(size)] for y in range(size)]

    def get_area(self, x, y):
        return self.grid[y][x]

    def set_area(self, x, y, area):
        self.grid[y][x] = area

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

# Ship class -- represents a ship in the game
class Ship:
    def __init__(self, name='Default Ship', length=3, symbol='S'):
        self.name = name
        self.length = length
        self.symbol = symbol
        self.areas = []  # List of Area objects that make up the ship

    def add_area(self, area):
        if len(self.areas) < self.length:
            self.areas.append(area)
            area.is_ship = True
            area.symbol = self.symbol
        else:
            print('Ship is already full!')
    
    def debugPrint(self):
        print('This Ship contains:')
        print(f'name: {self.name}')
        print(f'length: {self.length}')
        print(f'symbol: {self.symbol}')
        print('Areas:')
        for area in self.areas:
            area.debugPrint()
        print()

# Player class -- represents a player in the game
class Player:
    def __init__(self, name = 'Nameless'):
        self.ships = []
        self.name = name
        self.friendly_grid = Grid(name = self.name + ' Friendly Grid')
        self.enemy_grid = Grid(name = self.name + ' Enemy Grid')
    
    def displayGrids(self):
        print(f'{self.name}\'s Enemy Grid:')
        self.enemy_grid.display()
        print()
        print(f'{self.name}\'s Friendly Grid:')
        self.friendly_grid.display()
        print()
        
    def insert_ship(self, ship):
        area_list = []
        print('Inserting ship...')
        for i in range(ship.length):
            try:
                ship_start = input('Enter coordinates (x y): ')
                x, y = map(int, ship_start.split())
                if 0 <= x < self.friendly_grid.size and 0 <= y < self.friendly_grid.size:
                    print(f'Placing ship at ({x}, {y})')
                    # Hold final changes until all ship spots are validated
                    # Check if the area is already occupied by another ship
                    if self.friendly_grid.get_area(x, y).is_ship:
                        print('Area already occupied by another ship. Please try again.')
                        return False
                    # TODO: Check if the area is directly adjacent to another area in area_list. Otherwise reject this area.
                else:
                    print('Coordinates out of bounds. Please try again.')
                    return False
            except ValueError:
                print('Invalid input. Please enter coordinates in the form "x y".')
                return False
            print('"Selected" area details')
            self.friendly_grid.get_area(x, y).debugPrint()
            print('New area(s) details')
            area_list.append(Area(x, y, is_ship=True, symbol='S'))
            for area in area_list:
                area.debugPrint()
        for area in area_list:
            self.friendly_grid.set_area(area.x, area.y, area)
            ship.add_area(area)
        return True

# Test zone
user_input = ''
print('\n\n')
print('Welcome to Naval Combat System!')
# user_input = input('>>>>Enter a name for your player: <<<<\n')
user_input = 'Amber'  # For testing purposes, we can hardcode the name
user = Player(name=user_input)
print(f'Hello, {user.name}!\n')
user.displayGrids()
print('Before we get started, let\'s set up your ships!')
print('You have 5 ships to place on your friendly grid. Coordinates are in the form of "x y" (x[space]y) where x is the column and y is the row.')
print('Let\'s start with the first ship.')
print('The first ship is 3 squares long. Provide the starting coordinates for the ship.')

# Test the insert_ship function
ship = Ship(name='Test Ship', length=3, symbol='S')
print('Ship details before insertion:')
ship.debugPrint()
print('Attempting to insert ship...')
result = user.insert_ship(ship)
print(f'Insert ship result: {result}')
user.displayGrids()
print('End of test zone')