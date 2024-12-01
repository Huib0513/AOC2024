#!python3
import os
import datetime

# Test input
input = [
"3   4",
"4   3",
"2   5",
"1   3",
"3   9",
"3   3"
]

# input complete lines
input = open('input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().splitlines()

def solve1():
    left = []
    right = []
    for row in input:
        l,r = row.split('   ')
        left.append(int(l))
        right.append(int(r))
    left.sort()
    right.sort()

    sum = 0
    for row in range(len(left)):
        sum += abs(left[row] - right[row])
    result = sum

    print("Deel 1: " + str(result))

def solve2():
    left = defaultdict(int)
    right = defaultdict(int)

    for row in input:
        l,r = row.split('   ')
        left[l] += 1
        right[r] += 1
    
    diff = 0
    for l in left.keys():
        diff += int(l) * left[l] * right[l]
    result = diff
    print("Deel 2: " + str(result))

start = datetime.datetime.now()
solve1()
print("Tijd voor oplossing 1: ", datetime.datetime.now()-start)

start = datetime.datetime.now()
solve2()
print("Tijd voor oplossing 2: ", datetime.datetime.now()-start)
