''' This project is designed and coded by:
    Amber Shifflett, 2024 '''
# main.py
import random

class GameSpot:
    def __init__(self):
        self.occupiedBy = ''
        #initialized to blank string by default,
        #since only 2/4 boards wil default to water
    def __init__(self, fillChar):
        self.occupiedBy = fillChar
    def setLocation(self, newOccupant):
        self.occupiedBy = newOccupant
    def getLocation(self):
        return self.occupiedBy
        
    def getSymbol(self):
        if self.occupiedBy == 'untested water':
            return '?'
        elif self.occupiedBy == 'hit':
            return 'X'
        elif self.occupiedBy == 'miss':
            return 'O'
        elif self.occupiedBy == 'water':
            return 'W'
        elif self.occupiedBy == 'ship':
            return 'S'
        elif self.occupiedBy == '':
            return 'E' # E for unassigned Error
        else:
            return 'U' # U for Unrecognized error

class GameBoard:
    def __init__(self):
        self.grid = [[GameSpot() for _ in range(12)] for _ in range(12)]
        #creates a 12x12 grid initialized with blank GameSpots
    def __init__(self, fillChar):
        self.grid = [[GameSpot(fillChar) for _ in range(12)] for _ in range(12)]
        #creates a 12x12 grid initialized with fillChar GameSpots
    def printGrid(self):
        print("   " + " ".join([chr(i + 65) for i in range(0, 12)]))
        for i in range(0, 12):
            row = self.grid[i]
            returnString = '' + str(i + 1) + ' '
            if ((i + 1) < 10):
                returnString += ' '
            for j in range(0,12):
                returnString += row[j].getSymbol() + ' '
            print(returnString)


