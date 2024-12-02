#!python3
import os
import datetime

# Test input
input = [
"7 6 4 2 1",
"1 2 7 8 9",
"9 7 6 2 1",
"1 3 2 4 5",
"8 6 4 4 1",
"1 3 6 7 9"
]

# input complete lines
input = open('input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().splitlines()

def solve1():
    count = 0
    for r in input:
        valid = True
        rs = [int(l) for l in r.split(' ')]
        dir = 1 if ((rs[1] - rs[0]) > 0) else -1
        for i in range(len(rs)-1):
            d = rs[i+1] - rs[i]

            if not ((0 < abs(d) <=3) and ((d*dir) == d)):
                valid = False
                break
        print(i, valid)
        if (valid == True): count += 1
    result = count

    print("Deel 1: " + str(result))

def solve2():
    result = 'No'
    print("Deel 2: " + str(result))

start = datetime.datetime.now()
solve1()
print("Tijd voor oplossing 1: ", datetime.datetime.now()-start)

start = datetime.datetime.now()
solve2()
print("Tijd voor oplossing 2: ", datetime.datetime.now()-start)
