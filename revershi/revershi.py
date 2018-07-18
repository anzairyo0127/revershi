emptie = 0
white = -1
black = 1
wall = 2

class Point():
    def __init__(self):
        (self.x,self.y) = (0,0)

    def point(self,x,y):
        (self.x,self.y) = (x,y)

class Disc(Point):    
    def __init__(self):
        self.color = emptie

    def disc(self,color):
        self.color = color

BORD_SIZE = 8
Raw_Board = [[BORD_SIZE+2],[BORD_SIZE+2]]
