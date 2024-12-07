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

def loopy(pos, dir, floorplan):
    positions = {}
    newpos = pos
    while ((0<= newpos[0] < len(input)) and (0<= newpos[1] < len(input[0]))):
        pos = newpos
        if (pos in positions.keys()):
            if (dir in positions[pos]):
                return True
            else:
                positions[pos].append(dir)
        else:
            positions[pos] = [dir]
        newpos = moves[dir](pos[0],pos[1])
        if (0<= newpos[0] < len(input)) and (0<= newpos[1] < len(input[0])):
            if floorplan[newpos] == '#':
                # shift directions one right, recalculate newpos
                dir = directions[(directions.index(dir) + 1) % 4]
                newpos = moves[dir](pos[0],pos[1])
            #print(newpos)
    return False

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

def solve2(startpos, dir):
    result = 0
    for r in range(len(input)):
        for c in range(len(input[0])):
            if (r,c) == startpos:
                # Can't add something under the feet of the guard
                continue
            if (maze[(r,c)] == '#'):
                # There is a blockade on this tile already
                continue
            # Change the current tile to a blockade and determine if this creates a loop
            #print('before: ' + str([x for x in maze[r, y] for y in len(input[0])]))                         
            maze[(r,c)] = '#'
            #print('after: ' + str([x for x in maze[r, y] for y in len(input[0])]))                         
            if (loopy(startpos, dir, maze)):
                result += 1
            maze[(r,c)] = '.'

    #result = 'No'
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
solve2(pos, dir)
print("Tijd voor oplossing 2: ", datetime.datetime.now()-start)
