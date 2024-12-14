#!python3
import os
import datetime

# Test input
input = ["190: 10 19",
"3267: 81 40 27",
"83: 17 5",
"156: 15 6",
"7290: 6 8 6 15",
"161011: 16 10 13",
"192: 17 8 14",
"21037: 9 7 18 13",
"292: 11 6 16 20"]

# input complete lines
#input = open('input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().splitlines()

def get_values(startval: list, parts: list):
    possiblevalues = []
    for s in startval:
        possiblevalues.append(s * parts[0])
        possiblevalues.append(s + parts[0])
    if len(parts) > 1:
        possiblevalues += (get_values(possiblevalues, parts[1:]))
    return possiblevalues

def solve1():
    result = 0
    for line in input:
        target = int(line.split(': ')[0])
        values = get_values([int(line.split(': ')[1].split(' ')[0])], [int(x) for x in line.split(': ')[1].split(' ')[1:]])
        if (target in values):
            print('Match! ' + str(target) + ' is in ', end='')
            print(values)
            result += int(line.split(': ')[0])
        else:
            print('No match :( ' + str(target) + ' is NOT in ', end='')
            print(values)
    print("Deel 1: " + str(result))

def solve2():
    print("Deel 2: No")

start = datetime.datetime.now()
solve1()
print("Tijd voor oplossing 1: ", datetime.datetime.now()-start)

start = datetime.datetime.now()
solve2()
print("Tijd voor oplossing 2: ", datetime.datetime.now()-start)
