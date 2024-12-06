#!python3
import os
import datetime
from collections import defaultdict

# Test input
input = [
"47|53",
"97|13",
"97|61",
"97|47",
"75|29",
"61|13",
"75|53",
"29|13",
"97|29",
"53|29",
"61|53",
"97|53",
"61|29",
"47|13",
"75|47",
"97|75",
"47|61",
"75|61",
"47|29",
"75|13",
"53|13",
"",
"75,47,61,53,29",
"97,61,53,29,13",
"75,29,13",
"75,97,47,61,53",
"61,13,29",
"97,13,75,29,47"]

# input complete lines
input = open('input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().splitlines()

def valid_update(line):
    valid = True
    for i in line:
        if i in rules.keys():
            for j in rules[i]:
                if ((j in line) and (line.index(j) < line.index(i))):
                    return False
    return valid

def reorder(line):
    for i in line:
        if i in rules.keys():
            pos = line.index(i)
            for j in rules[i]:
                if ((j in line) and line.index(j) < pos):
                    pos = line.index(j)
            #pos = min([line.index(v) for v in rules[i] if v in line])
            line.pop(line.index(i))
            line.insert(pos, i)
    return 

def solve1():
    result1 = 0
    result2 = 0
    for u in updates:
        if (valid_update(u)):
            result1 +=int( u[(len(u)//2)])
        else:
            reorder(u)
            print(u)
            result2 += int( u[(len(u)//2)])
    #result = 'No'
    print("Deel 1: " + str(result1))
    print("Deel 2: " + str(result2))

def solve2():
    result = 'No'
    print("Deel 2: " + str(result))

start = datetime.datetime.now()
rules = defaultdict(list)
updates = []
for line in input:
    if (line.find('|') != -1):
        rules[line.split('|')[0]].append(line.split('|')[1], )
    elif (line != ""):
        updates.append(line.split(','))
solve1()
print("Tijd voor oplossing 1: ", datetime.datetime.now()-start)

start = datetime.datetime.now()
solve2()
print("Tijd voor oplossing 2: ", datetime.datetime.now()-start)
