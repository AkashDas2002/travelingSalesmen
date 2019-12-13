import sys
import math

class Point:
    def __init__(self, xcor, ycor):
        self.xcor = xcor;
        self.ycor = ycor;

def dist(point1, point2):
    return math.sqrt((point1.xcor - point2.xcor) ** 2 + (point1.ycor - point2.ycor) ** 2)

def reverseSubArray(list, i, j):
    list[i:j] = list[i:j][::-1]

def firstPath(pointsArray):
    numPoints = len(pointsArray)
    pathIndex = [i for i in range(numPoints)]
    for i in range(numPoints - 1):
        minIndex = i + 1
        minDist = dist(pointsArray[i], pointsArray[minIndex])
        j = i + 1
        while j < numPoints:
            if dist(pointsArray[i], pointsArray[j]) < minDist:
                minIndex = j
                minDist = dist(pointsArray[i], pointsArray[j])
            j += 1
        pointsArray[i+1], pointsArray[minIndex] = pointsArray[minIndex], pointsArray[i+1]
        pathIndex[i+1], pathIndex[minIndex] = pathIndex[minIndex], pathIndex[i+1]

    return [pathIndex, pointsArray]

def makeCycle(pathIndex, pointsArray):
    pathIndex.append(pathIndex[0])
    pointsArray.append(pointsArray[0])

def uncross(pathIndex, pointsArray):
    numPoints = len(pathIndex);
    for i in range(numPoints - 3):
        for j in range(i+2, numPoints - 1):
            if isCross(pointsArray[i],pointsArray[i+1],pointsArray[j], pointsArray[j+1]):
                reverseSubArray(pointsArray, i+1, j+1)
                reverseSubArray(pathIndex, i+1, j+1)


def crossP(p1, p2, p3):
    return (p1.xcor - p2.xcor)*(p3.ycor - p2.ycor) - (p1.ycor - p2.ycor)*(p3.xcor - p2.xcor)

def isCross(p1,p2,p3,p4):
    c1 = crossP(p1,p3,p4)
    c2 = crossP(p2,p3,p4)
    c3 = crossP(p3,p1,p2)
    c4 = crossP(p4,p1,p2)
    return ((c1 < 0 and c2 > 0) or (c1 > 0 and c2 < 0)) and ((c3 < 0 and c4 > 0) or (c3 > 0 and c4 < 0))

def findShortPath(pointsArray):
    a = firstPath(pointsArray)
    makeCycle(a[0],a[1])
    uncross(a[0],a[1])
    return a

p1 = Point(0, 0)
p2 = Point(4, 4)
p3 = Point(4, 0)
p4 = Point(0, 4)
print(findShortPath([p1,p2,p3,p4]))


3,9,14,4,13,3,9,13
13,3,3,6,0,3,6,6
q1 = Point(3,13)
q2 = Point(9,3)
q3 = Point(14,3)
q4 = Point(4,6)
q5 = Point(13,0)
q6 = Point(3,3)
q7 = Point(9,6)
q8 = Point(13,6)
print(findShortPath([q1,q2,q3,q4,q5,q6,q7,q8]))
