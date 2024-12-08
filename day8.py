#!python3
import os
import datetime
from collections import defaultdict

# Test input
input = ["............",
"........0...",
".....0......",
".......0....",
"....0.......",
"......A.....",
"............",
"............",
"........A...",
".........A..",
"............",
"............"]

# input complete lines
input = open('input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().splitlines()

def getnodes(a: tuple, b:tuple, maxrow: int, maxcol: int) -> list:
    rowup = min(a[0], b[0]) - abs(a[0] - b[0])
    rowdown = max(a[0], b[0]) + abs(a[0] - b[0])
    colright = max(a[1], b[1]) + abs(a[1] - b[1])
    colleft = min(a[1], b[1]) - abs(a[1] - b[1])

    if ((a[0] > b[0]) and (a[1] > b[1])):
        options = [(rowup, colleft), (rowdown, colright)]
    elif ((a[0] <= b[0]) and (a[1] > b[1])):
        options = [(rowup, colright), (rowdown, colleft)]
    elif ((a[0] > b[0]) and (a[1] <= b[1])):
        options = [(rowup, colright), (rowdown, colleft)]
    else:
        options = [(rowup, colleft), (rowdown, colleft)]
    return ([(x,y) for (x,y) in options if ((0 <= x < maxrow) and (0 <= y < maxcol))])

def findantinodes(antennalist: list, maxrow: int, maxcol: int) -> list:
    nodes = []
    if (len(antennalist) != 1):
        for a in antennalist[1:]:
            nodes += getnodes(antennalist[0], a, maxrow, maxcol)
        nodes += findantinodes(antennalist[1:], maxrow, maxcol)
    return nodes

def solve1():
    locations = defaultdict(list)
    for row in range(len(input)):
        for col in range(len(input[row])):
            if (input[row][col] != '.'):
                locations[input[row][col]].append((row,col))
    #print(locations)
    
    result = set()
    for x in locations:
        result.update(findantinodes(locations[x], len(input), len(input[0])))
    print(result)
    print("Deel 1: " + str(len(result)))

def solve2():
    print("Deel 2: No")

start = datetime.datetime.now()
solve1()
print("Tijd voor oplossing 1: ", datetime.datetime.now()-start)

start = datetime.datetime.now()
solve2()
print("Tijd voor oplossing 2: ", datetime.datetime.now()-start)
