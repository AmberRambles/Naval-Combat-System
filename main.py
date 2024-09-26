''' This project is designed and coded by:
    Amber Shifflett, 2024 '''
# main.py
import random

DEBUG = True

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
        self.typeName = 'ship'
        self.name = name
        self.length = length
        self.occupying = []

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
        self.deployedShips = []
    def printMyTerritory(self):
        print('Your Territory')
        self.myFleetViewGameBoard.printGrid()
    def printEnemyTerritory(self):
        print('Enemy Territory')
        self.myEnemyViewGameBoard.printGrid()
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
                userIn = input('Enter the number of the ship you would like to place: ')
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
        if DEBUG:
            print(f'shipIndex = {shipIndex}')
        print()
        print(f'{self.shipList[shipIndex].name} needs {self.shipList[shipIndex].length} spaces')
        print('You will enter the coordinates for the first space your ship will enter, followed by a direction.')
        self.printMyTerritory()
        badDirection2 = True
        while badDirection2:
            badCoordinates = True
            while badCoordinates:
                userIn = input('Enter the coordinate, separated by a comma (ex, A,1): ').upper()
                if DEBUG:
                    print(f'userIn = {userIn}')
                userIn = userIn.replace(' ', '')
                if DEBUG:
                    print(f'userIn = {userIn}')
                userIn = userIn.split(',')
                if DEBUG:
                    print(f'userIn = {userIn}')
                desiredX = userIn[0]
                if DEBUG:
                    print(f'desiredX = {desiredX}')
                desiredY = userIn[1]
                if DEBUG:
                    print(f'desiredY = {desiredY}')
                    print(f'Calling: self(Player-class).myFleetViewGameBoard.spotExists({desiredX}, {desiredY})')
                    print(self.myFleetViewGameBoard.spotExists(desiredX, desiredY))
                if self.myFleetViewGameBoard.spotExists(desiredX, desiredY):
                    badCoordinates = False
                else:
                    print('Something is wrong with your coordinates.')
            badDirection1 = True
            while badDirection1:
                userIn = input('Enter the direction you would like for the ship to be inserted, ex. up, down, left, right: ').lower()
                if DEBUG:
                    print(f'userIn = {userIn}')
                if userIn == 'up' or userIn == 'u':
                    #get length of ship for loop
                    shipLen = self.shipList[shipIndex].length
                    coordList = []
                    if DEBUG:
                        print(f'shipLen = {shipLen}')
                        print(f'coordList = {coordList}')
                    for i in range(shipLen):
                        #check validity of each space
                        if DEBUG:
                            print(f'i = {i}')
                            print(f'shipLen = {shipLen}')
                            print(f'coordList = {coordList}')
                            print(f'desiredX = {desiredX}')
                            print(f'desiredY = {desiredY}')
                        desiredY = int(desiredY)
                        if DEBUG:
                            print(f'desiredY = {desiredY}')
                        thisY = desiredY - i
                        if DEBUG:
                            print(f'thisY = {thisY}')
                            print(f'Calling: self.myFleetViewGameBoard.spotExists({desiredX}, {thisY})')
                            print(self.myFleetViewGameBoard.spotExists(desiredX, thisY))
                        if self.myFleetViewGameBoard.spotExists(desiredX, thisY):
                            #check availability of each space
                            if DEBUG:
                                print(f'Calling: self.myFleetViewGameBoard.coordinates({desiredX}, {thisY}).getLocation()')
                                print(self.myFleetViewGameBoard.coordinates(desiredX, thisY).getLocation())
                                print('If that is water...')
                            if self.myFleetViewGameBoard.coordinates(desiredX, thisY).getLocation() == 'water':
                                if DEBUG:
                                    print('appending to coordList')
                                coordList.append([desiredX, thisY])
                                if DEBUG:
                                    print(coordList)
                            else:
                                print('Not all spots are free')
                                badDirection1 = True
                                break
                        else:
                            print('Not all spots Exist')
                            badDirection1 = True
                            break
                    else:
                        if DEBUG:
                            print('setting badDirection1 to False')
                        badDirection1 = False
                elif userIn == 'down' or userIn == 'd':
                    #get length of ship for loop
                    shipLen = self.shipList[shipIndex].length
                    coordList = []
                    if DEBUG:
                        print(f'shipLen = {shipLen}')
                        print(f'coordList = {coordList}')
                    for i in range(shipLen):
                        #check validity of each space
                        if DEBUG:
                            print(f'i = {i}')
                            print(f'shipLen = {shipLen}')
                            print(f'coordList = {coordList}')
                            print(f'desiredX = {desiredX}')
                            print(f'desiredY = {desiredY}')
                        desiredY = int(desiredY)
                        if DEBUG:
                            print(f'desiredY = {desiredY}')
                        thisY = desiredY + i
                        if DEBUG:
                            print(f'thisY = {thisY}')
                            print(f'Calling: self.myFleetViewGameBoard.spotExists({desiredX}, {thisY})')
                            print(self.myFleetViewGameBoard.spotExists(desiredX, thisY))
                        if self.myFleetViewGameBoard.spotExists(desiredX, thisY):
                            #check availability of each space
                            if DEBUG:
                                print(f'Calling: self.myFleetViewGameBoard.coordinates({desiredX}, {thisY}).getLocation()')
                                print(self.myFleetViewGameBoard.coordinates(desiredX, thisY).getLocation())
                                print('If that is water...')
                            if self.myFleetViewGameBoard.coordinates(desiredX, thisY).getLocation() == 'water':
                                if DEBUG:
                                    print('appending to coordList')
                                coordList.append([desiredX, thisY])
                                if DEBUG:
                                    print(coordList)
                            else:
                                print('Not all spots are free')
                                badDirection1 = True
                                break
                        else:
                            print('Not all spots Exist')
                            badDirection1 = True
                                break
                    else:
                        if DEBUG:
                            print('setting badDirection1 to False')
                        badDirection1 = False
                elif userIn == 'left' or userIn == 'l':
                    #get length of ship for loop
                    shipLen = self.shipList[shipIndex].length
                    coordList = []
                    if DEBUG:
                        print(f'shipLen = {shipLen}')
                        print(f'coordList = {coordList}')
                    for i in range(shipLen):
                        #check validity of each space
                        if DEBUG:
                            print(f'i = {i}')
                            print(f'shipLen = {shipLen}')
                            print(f'coordList = {coordList}')
                            print(f'desiredX = {desiredX}')
                            print(f'desiredY = {desiredY}')
                            print('Convert desiredX to ASCII, subtract i, and convert back to char, then save to thisX')
                        thisX = chr(ord(desiredX) - i)  # Convert desiredX to ASCII, subtract i, and convert back to char, then save to thisX
                        if DEBUG:
                            print(f'thisX = {thisX}')
                            print(f'Calling: self.myFleetViewGameBoard.spotExists({thisX}, {desiredY})')
                            print(self.myFleetViewGameBoard.spotExists(thisX, desiredY))
                        if self.myFleetViewGameBoard.spotExists(thisX, desiredY):
                            #check availability of each space
                            if DEBUG:
                                print(f'Calling: self.myFleetViewGameBoard.coordinates({thisX}, {desiredY}).getLocation()')
                                print(self.myFleetViewGameBoard.coordinates(thisX, desiredY).getLocation())
                                print('If that is water...')
                            if self.myFleetViewGameBoard.coordinates(thisX, desiredY).getLocation() == 'water':
                                if DEBUG:
                                    print('appending to coordList')
                                coordList.append([thisX, desiredY])
                                if DEBUG:
                                    print(coordList)
                            else:
                                print('Not all spots are free')
                                badDirection1 = True
                                break
                        else:
                            print('Not all spots Exist')
                            badDirection1 = True
                            break
                    else:
                        if DEBUG:
                            print('setting badDirection1 to False')
                        badDirection1 = False
                elif userIn == 'right' or userIn == 'r':
                    #get length of ship for loop
                    shipLen = self.shipList[shipIndex].length
                    coordList = []
                    if DEBUG:
                        print(f'shipLen = {shipLen}')
                        print(f'coordList = {coordList}')
                    for i in range(shipLen):
                        #check validity of each space
                        if DEBUG:
                            print(f'i = {i}')
                            print(f'shipLen = {shipLen}')
                            print(f'coordList = {coordList}')
                            print(f'desiredX = {desiredX}')
                            print(f'desiredY = {desiredY}')
                            print('Convert desiredX to ASCII, add i, and convert back to char, then save to thisX')
                        thisX = chr(ord(desiredX) + i)  # Convert desiredX to ASCII, add i, and convert back to char, then save to thisX
                        if DEBUG:
                            print(f'thisX = {thisX}')
                            print(f'Calling: self.myFleetViewGameBoard.spotExists({thisX}, {desiredY})')
                            print(self.myFleetViewGameBoard.spotExists(thisX, desiredY))
                        if self.myFleetViewGameBoard.spotExists(thisX, desiredY):
                            #check availability of each space
                            if DEBUG:
                                print(f'Calling: self.myFleetViewGameBoard.coordinates({thisX}, {desiredY}).getLocation()')
                                print(self.myFleetViewGameBoard.coordinates(thisX, desiredY).getLocation())
                                print('If that is water...')
                            if self.myFleetViewGameBoard.coordinates(thisX, desiredY).getLocation() == 'water':
                                if DEBUG:
                                    print('appending to coordList')
                                coordList.append([thisX, desiredY])
                                if DEBUG:
                                    print(coordList)
                            else:
                                print('Not all spots are free')
                                badDirection1 = True
                                break
                        else:
                            print('Not all spots Exist')
                            badDirection1 = True
                            break
                    else:
                        if DEBUG:
                            print('setting badDirection1 to False')
                        badDirection1 = False
                else:
                    print('I did not understand that direction.')
            for item in coordList:
                x = item[0]
                y = item[1]
                self.shipList[shipIndex].occupying.append([x, y])
            badDirection2 = False
        for coord in self.shipList[shipIndex].occupying:
            x = coord[0]
            y = coord[1]
            self.myFleetViewGameBoard.coordinates(x, y).setLocation(self.shipList[shipIndex].typeName)
        self.deployedShips.append(self.shipList.pop(shipIndex))
        #end of insertShip
    #start of next Player method

#for testing:
user = Player('Amber', False)
user.insertShip()
print('success')
user.myFleetViewGameBoard.printGrid()
finalIn = input('Again? Yes/No: ').lower()
if finalIn == 'yes' or finalIn == 'y':
    again = True
else:
    again = False
if again:
    user.insertShip()
    user.myFleetViewGameBoard.printGrid()