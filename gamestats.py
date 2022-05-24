import pygame

class gameStats():
    def __init__(self):
        self.worldspeed = 4
        self.ground_pos = 650
        self.points = 0
        self.hspath = "hs.txt"
        with open(self.hspath) as f:
            lines = f.readlines()
            if lines is not None:
                self.hs = lines
        str1 = ""
        for ele in self.hs: 
            str1 += ele  
        self.hs = int(str1)


    def addPoints(self):
        self.points += 1
        #print(self.points)

    def setHighScore(self):
        if self.points > self.hs:
            self.hs = str(self.points)
            print("hs is ",self.hs)
            with open("hs.txt", 'w') as f:
                f.write(self.hs)