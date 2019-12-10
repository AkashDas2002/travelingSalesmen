import sys
import math

class Points:
    def __init__(self, xcor, ycor):
        self.xcor = xcor;
        self.ycor = ycor;

def dist(point1, point2):
    return math.sqrt((point1.xcor - point2.xcor) ** 2 + (point1.ycor - point2.ycor) ** 2)

def firstPath(pointArray):
    path = [0]
    length = len(pointsArray)
    while len(path) < length:
        i = len(path)
        minIndex = i
        minDist = dist(path[-1], pointArray[i])
        while(i < length):
