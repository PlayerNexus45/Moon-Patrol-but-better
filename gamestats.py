import pygame

class gameStats():
    def __init__(self):
        self. worldspeed = 4
        self.ground_pos = 650
        self.points = 0
        self.hspath = "hs.txt"
        with open(self.hspath) as f:
            lines = f.readlines()
            if lines is not None:
                self.hs = lines
    def addPoints(self):
        self.points += 1
        print(self.points)
