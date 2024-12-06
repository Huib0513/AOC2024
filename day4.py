#!python3
import os
import datetime
import re

# Test input
input = ["MMMSXXMASM",
"MSAMXMSMSA",
"AMXSXMAAMM",
"MSAMASMSMX",
"XMASAMXAMM",
"XXAMMXXAMA",
"SMSMSASXSS",
"SAXAMASAAA",
"MAMMMXMMMM",
"MXMXAXMASX"]

# input complete lines
#input = open('input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().splitlines()

def solve1():
    horizontals = verticals = 0
    for line in input:
        horizontals += len(re.findall('XMAS', line))
        horizontals += len(re.findall('SAMX', line))
    print(horizontals)
    verticallines = [''.join(x) for x in [[l[r] for l in input] for r in range(len(input[0]))]]
    for line in verticallines:
        verticals += len(re.findall('XMAS', line))
        verticals += len(re.findall('SAMX', line))
    print(verticals)
    result = 'No'
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
