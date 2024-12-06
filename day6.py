#!python3
import os
import datetime

# Test input
input = [
"....#.....",
".........#",
"..........",
"..#.......",
".......#..",
"..........",
".#..^.....",
"........#.",
"#.........",
"......#..."]

# input complete lines
input = open('input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().splitlines()

directions = ['u', 'r', 'd', 'l']
moves = {'u':(lambda x,y: (x-1,y)), 'r': (lambda x,y: (x,y+1)), 'd': (lambda x,y: (x+1,y)), 'l': (lambda x,y: (x, y-1))}

def solve1(pos, dir):
    positions = set()
    newpos = pos
    while ((0<= newpos[0] < len(input)) and (0<= newpos[1] < len(input[0]))):
        pos = newpos
        positions.add(pos)
        newpos = moves[dir](pos[0],pos[1])
        if (0<= newpos[0] < len(input)) and (0<= newpos[1] < len(input[0])):
            if maze[newpos] == '#':
                # shift directions one right, recalculate newpos
                dir = directions[(directions.index(dir) + 1) % 4]
                newpos = moves[dir](pos[0],pos[1])
            #print(newpos)
    result = len(positions)
    print("Deel 1: " + str(result))

def solve2():
    result = 'No'
    print("Deel 2: " + str(result))

maze = {}
dir = 'u'
for r in range(len(input)):
    for c in range(len(input[r])):
        if input[r][c] == '^':
            pos = (r,c)
            maze[(r,c)] = '.'
        else:
            maze[(r,c)] = input[r][c]

start = datetime.datetime.now()
solve1(pos, dir)
print("Tijd voor oplossing 1: ", datetime.datetime.now()-start)

start = datetime.datetime.now()
solve2()
print("Tijd voor oplossing 2: ", datetime.datetime.now()-start)
