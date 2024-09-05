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
        self.grid = pass