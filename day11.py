#!python3
import os
import datetime

# Test input
#input = ["0 1 10 99 999"]
#input = ["125 17"]

#REAL input!
input = ["0 27 5409930 828979 4471 3 68524 170"]

# input integers separated by commas
#input= [int(i) for i in open("input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().split(",")]

# input integers on complete lines
#input = [int(i) for i in open('input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().splitlines()]

# input complete lines
#input = open('input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().splitlines()


def solve1():
    blinks = 75
    stones = [int(s) for s in input[0].split(' ')]
    for blink in range(blinks):
#        print(str(blink) + ": ", end='')
#        print(stones)
        newstones = []
        for s in range(len(stones)):
            if stones[s] == 0:
                newstones.append(1)
            elif (len(str(stones[s]))%2) == 0:
                newstones.append(int(str(stones[s])[:len(str(stones[s]))//2]))
                newstones.append(int(str(stones[s])[len(str(stones[s]))//2:]))
            else:
                newstones.append(stones[s]*2024)
        stones = newstones
    print("Deel 1: " + str(len(stones)))
    

def solve2():
    print("Deel 2: No")

start = datetime.datetime.now()
solve1()
print("Tijd voor oplossing 1: ", datetime.datetime.now()-start)

start = datetime.datetime.now()
solve2()
print("Tijd voor oplossing 2: ", datetime.datetime.now()-start)
