''' This project is designed and coded by:
    Amber Shifflett, 2024 '''
# main.py
import random

class GameSpot:
    def __init__(self, fillChar = ''):
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
    def __init__(self, fillChar = ''):
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
    def spotExists(self, x, y):
        x = x.toUpper()
        x = ord(x) - 65
        if x > -1:
            if x < 12:
                xOkay = True
            else:
                xOkay = False
        else:
            xOkay = False
        y = int(y) - 1
        if y > -1:
            if y < 12:
                yOkay = True
            else:
                yOkay = False
        else:
            yOkay = False
            return xOkay and yOkay
    def coordinates(self, x, y):
        x = ord(x) - 65 #'A-L' to 0-11
        y = int(y) - 1 #'1-12' to 0-11
        return self.grid[y][x]

class Ship:
    def __init__(self, name = '', length = 1):
        self.type = 'ship'
        self.name = name
        self.length = length
        
shipList = []
shipList.append(Ship('Aircraft Carrier', 6))
shipList.append(Ship('Destroyer', 5))
shipList.append(Ship('Battleship', 4))
shipList.append(Ship('Submarine', 3))
shipList.append(Ship('Cruiser', 3))
shipList.append(Ship('Patrol Scout', 2))

class Player:
    def __init__(self, name = 'CPU', isComputer = True):
        self.name = name
        self.isComputer = isComputer
        self.myFleetViewGameBoard = GameBoard('water')
        self.myEnemyViewGameBoard = GameBoard('untested water')