''' This project is designed and coded by:
    Amber Shifflett, 2024 '''
# main.py
import random

class GameSpot:
    def __init__(self):
        self.occupiedBy = ''  #initialized to blank string by default, since only 2/4 boards wil default to water
    def setLocation(self, newOccupant):
        self.occupiedBy = newOccupant
    def getLocation(self):
        return self.occupiedBy

class GameBoard:
    def __init__(self, fillChar):
        self.grid = [[GameSpot() for _ in range(12)] for _ in range(12)]
        #creates a 12x12 grid initialized with blank GameSpots
    def getSymbol(self, spot):
        if spot.occupiedBy == 'untested water':
            return '?'
        elif spot.occupiedBy == 'hit':
            return 'X'
        elif spot.occupiedBy == 'miss':
            return 'O'
        elif spot.occupiedBy == 'water':
            return 'W'
        elif spot.occupiedBy == 'ship':
            return 'S'
        elif spot.occupiedBy == '':
            return 'E' # E for unassigned Error
        else:
            return 'U' # U for Unrecognized error
    def printGrid(self):
        pass