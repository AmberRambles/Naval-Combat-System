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
        x = x.upper()
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
        x = x.upper()
        x = ord(x) - 65 #'A-L' to 0-11
        y = int(y) - 1 #'1-12' to 0-11
        return self.grid[y][x]

class Ship:
    def __init__(self, name = '', length = 1):
        self.type = 'ship'
        self.name = name
        self.length = length

class Player:
    def __init__(self, name = 'CPU', isComputer = True):
        self.name = name
        self.isComputer = isComputer
        self.myFleetViewGameBoard = GameBoard('water')
        self.myEnemyViewGameBoard = GameBoard('untested water')
        self.shipList = []
        self.shipList.append(Ship('Aircraft Carrier', 6))
        self.shipList.append(Ship('Destroyer', 5))
        self.shipList.append(Ship('Battleship', 4))
        self.shipList.append(Ship('Submarine', 3))
        self.shipList.append(Ship('Cruiser', 3))
        self.shipList.append(Ship('Patrol Scout', 2))
    def printMyTerritory(self):
        print('Your Territory')
        self.myFleetViewGameBoard.printGrid()
    def printEnemyTerritory(self):
        pass
    def insertShip(self):
        self.printMyTerritory()
        print('Your unplaced ships:')
        i = 1
        for ship in self.shipList:
            print(f'{i}  Name: {ship.name}, Length: {ship.length}')
            i += 1
        badInput2 = True
        while badInput2:
            badInput1 = True
            while badInput1:
                userIn = input('Enter the number of the ship you would like to place.')
                if (userIn.isnumeric()):
                    badInput1 = False
                else:
                    print('Please give a numerical response.')
            userIn = int(userIn)
            userIn -= 1
            if userIn >= 0 and userIn <= 5:
                badInput2 = False
            else:
                print('Please enter a valid number from the list.')
        shipIndex = userIn
        print(f'{self.shipList[shipIndex].name} needs {self.shipList[shipIndex].length} spaces')
        print('You will enter the coordinates for the first space your ship will enter, followed by a direction.')
        self.printMyTerritory()
        badDirection2 = True
        while badDirection2:
            badCoordinates = True
            while badCoordinates:
                userIn = input('Enter the coordinate, separated by a comma (ex, A,1):')
                userIn = userIn.replace(' ', '')
                userIn = userIn.split(',')
                    
                desiredX = userIn[0]
                desiredY = userIn[1]
                    
                if self.myFleetViewGameBoard.spotExists(desiredX, desiredY):
                    badCoordinates = False
                else:
                    print('Something is wrong with your coordinates.')
            badDirection1 = True
            while badDirection1:
                userIn = input('Enter the direction you would like for the ship to be inserted, ex. up, down, left, right').lower()
                if userIn == 'up' or userIn =='u':
                    #get length of ship for loop
                    shipLen = self.shipList[shipIndex].length
                    for i in range(shipLen):
                        #check validity of each space
                        thisY = desiredY - i
                        if self.myFleetViewGameBoard.spotExists(desiredX, thisY):
                            #check availability of each space
                            if self.myFleetViewGameBoard.coordinates(desiredX, thisY).getLocation == 'water':
                                pass
                            else:
                                print('Not all spots are free')
                        else:
                            print('Not all spots Exist')
                    #set badDirection1 to False
                elif userIn == 'down' or userIn == 'd':
                    pass
                elif userIn == 'left' or userIn == 'l':
                    pass
                elif userIn == 'right' or userIn == 'r':
                    pass
                else:
                    print('I did not understand that direction.')

#for testing:
user = Player('Amber', False)
user.insertShip()