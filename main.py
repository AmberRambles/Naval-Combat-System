''' This project is designed and coded by:
    Amber Shifflett, 2024 '''
# main.py
import random

DEBUG = True

def printBug():
    print('DEBUG PRINT')

def randInit():
    random.seed()
    # 'burn' some numbers to prime the generator
    random.randrange(100)
    random.randrange(100)
    random.randrange(100)

class GameSpot:
    def __init__(self, fillChar = ''):
        self.occupiedBy = fillChar
    def setLocation(self, newOccupant = ''):
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
        self.hits = 0

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
        if DEBUG:
            print('Printing self.deployedShips')
            print(self.deployedShips)
        #end of insertShip
    def isHit(self, x, y):
        if self.myFleetViewGameBoard.coordinates(x, y).getLocation() == 'ship':
            return True
        else:
            return False

class Game:
    def __init__(self):
        self.gameOver = False
        self.playerList = []
        self.turnCount = 0
        if DEBUG:
            printBug()
            print('Game start')
        # continue here for game init
    def createHumanPlayer(self):
        name = ''
        name = input('What will you be called?\n')
        self.playerList.append(Player(name, False))
        print(f'Thank You, Commander {name}.')
    def createCompPlayer(self):
        self.playerList.append(Player())
    def humanTurn(self):
        # Present both views
        self.playerList[0].myEnemyViewGameBoard.printGrid()
        print()
        self.playerList[0].myFleetViewGameBoard.printGrid()
        print()
        # Prompt for attack coords
        # input and spotExists validation
        badCoordinates = True
        while badCoordinates:
            userIn = input('Enter the coordinate for the space you want to attack, separated by a comma (ex, A,1): ').upper()
            userIn = userIn.replace(' ', '')
            userIn = userIn.split(',')
            desiredX = userIn[0]
            desiredY = userIn[1]
            if self.playerList[0].myEnemyViewGameBoard.spotExists(desiredX, desiredY): #if the desiredX and desiredY are valid
                spot = self.playerList[0].myEnemyViewGameBoard.coordinates(desiredX, desiredY).getSymbol()
                if spot == 'X' or spot == 'O': #if the valid coordinates have been used before
                    print('This spot was already attacked.')
                else:
                    badCoordinates = False
            else:
                print('Something is wrong with your coordinates.')
        # check if comp player is hit
        if self.playerList[1].myFleetViewGameBoard.coordinates(desiredX, desiredY).getLocation() == 'ship':
            #hit
            # update GameBoards as needed for hit
            self.playerList[0].myEnemyViewGameBoard.coordinates(desiredX, desiredY).setLocation('hit')
            self.playerList[1].myFleetViewGameBoard.coordinates(desiredX, desiredY).setLocation('hit')
            #find shipindex that was hit
            shipIndex = -1
            i = 0
            for ship in self.playerList[1].deployedShips:
                #checks all compy ships
                for coord in ship.occupying:
                    #check if the desiredX, desiredY matches any coords of this ship
                    if desiredX == coord[0] and desiredY == coord[1]:
                        shipIndex = i
                i += 1
            # update shipHits
            self.playerList[1].deployedShips[shipIndex].hits += 1
            # report turn update to user
            print("It's a hit!")
            # check if this hit sunk that ship
            if self.playerList[1].deployedShips[shipIndex].hits == self.playerList[1].deployedShips[shipIndex].length: #if this hit DID sink the ship
                print(f'You sunk their {self.playerList[1].deployedShips[shipIndex].name}!')
                self.playerList[1].deployedShips.pop(shipIndex) #remove the ship from computer player's deployedShips
                #check if this sinking caused the human to win
                if len(self.playerList[1].deployedShips) == 0: #if the computer has no remaining ships
                    print(f'Game Over! {self.playerList[0].name} has Won')
                    self.gameOver = True
        else:
            #miss
            # update GameBoards as needed for miss
            self.playerList[0].myEnemyViewGameBoard.coordinates(desiredX, desiredY).setLocation('miss')
            self.playerList[1].myFleetViewGameBoard.coordinates(desiredX, desiredY).setLocation('miss')
            #report miss to player
            print("It's a miss.")
    def compTurn(self):
        # generate random attack coords
        badCoords = True
        while badCoords:
            desiredX = random.randrange(12)
            desiredY = random.randrange(12)
            # TODO Add run check on coordinates, then an if block to change the badCoords flag to False
            result = False
            # spotExists validation
            result = self.playerList[0].myFleetViewGameBoard.spotExists(desiredX, desiredY)
            if result == True:
                #check if the spot has been guessed already
                result2 = False
                selectedSpace = self.playerList[1].myEnemyViewGameBoard.coordinates(desiredX, desiredY).getSymbol()
                if (selectedSpace == 'X') or (selectedSpace == 'O'):
                    if DEBUG:
                        printBug()
                        print('CPU selected a space they already guessed')
                else:
                    # Good space!
                    if DEBUG:
                        printBug()
                        print('CPU selected a good space!!')
                    badCoords = False
            else:
                if DEBUG:
                    printBug()
                    print('CPU selected a non-existing space. Trying again.')
        # check if human player was hit
        hit = False
        if self.playerList[0].myFleetViewGameBoard.coordinates(desiredX, desiredY).getSymbol() == 'S':
            hit = True
        # update GameBoards as needed for hit or miss
        if hit:
            pass
            # mark gameBoards for hit
            # check if human player lost
            # report turn update to user
        else:
            pass
            # mark gameBoards for miss
            # report turn update to user

#main logic
game = Game()
game.createHumanPlayer()
game.createCompPlayer()
randInit()
while game.gameOver == False:
    pass
