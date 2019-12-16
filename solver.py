import sys
import math

class Point:
    def __init__(self, xcor, ycor):
        self.xcor = xcor;
        self.ycor = ycor;

def dist(point1, point2):
    return math.sqrt((point1.xcor - point2.xcor) ** 2 + (point1.ycor - point2.ycor) ** 2)

def pathDist(path):
    i = 0
    total = 0
    while i < len(path) - 1:
        total += dist(path[i], path[i+1])
        i += 1
    return total

def reverseSubArray(list, i, j):
    list[i:j] = list[i:j][::-1]

def firstPath(pointsArray2, start):
    pointsArray = [pointsArray2[(i + start) % len(pointsArray2)] for i in range(len(pointsArray2))]
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
    return ((c1 <= 0 and c2 >= 0) or (c1 >= 0 and c2 <= 0)) and ((c3 <= 0 and c4 >= 0) or (c3 >= 0 and c4 <= 0))

def crossExists(pointsArray):
    numPoints = len(pointsArray);
    for i in range(numPoints - 3):
        for j in range(i+2, numPoints - 1):
            if isCross(pointsArray[i],pointsArray[i+1],pointsArray[j], pointsArray[j+1]):
                return True;
    return False;


def keepUncross(x,y):
    while crossExists(y):
        uncross(x,y)

def findShortPath(pointsArray):
    a = firstPath(pointsArray, 0)
    makeCycle(a[0],a[1])
    uncross(a[0],a[1])
    uncross(a[0],a[1])
    uncross(a[0],a[1])
    minDist = pathDist(a[1])
    minPath = a[0]
    for i in range(len(pointsArray)):
        d = firstPath(pointsArray, i)
        makeCycle(d[0],d[1])
        uncross(d[0],d[1])
        uncross(d[0],d[1])
        uncross(d[0],d[1])
        if pathDist(d[1]) < minDist:
            minDist = pathDist(d[1])
            minPath = [(el + i) % len(pointsArray) for el in d[0]]

    final = minPath
    while(final[0] != 0):
         for i in range(len(minPath)):
             final[i] = final[(i + 1) % len(minPath)]
    return final




input = open(sys.argv[1], "r")
output = open(sys.argv[2], "w")
a = input.readlines()
a = [el.strip() for el in a]
a  = [el.split(",") for el in a]
#print(a)
someString = ""
length = len(a)
index = 0
while index < length - 1:
    if index % 5 == 0:
        someString += a[index][0]
        someString += "\n"
    numPoints = len(a[index + 1])
    points = []
    i = 0
    while i < numPoints:
        points.append(Point(int(a[index+1][i]), int(a[index+2][i])))
        i += 1
    w = findShortPath(points)[:-1]
    print(w)
    w = [str(el) for el in w]
    someString += ",".join(w) + "\n\n"
    index += 5

output.write(someString)
