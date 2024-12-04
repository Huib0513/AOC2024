#!python3
import os
import datetime
import re

# Test input
# input = ["xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"]
input = ["xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"]

# input complete lines
### THIS PROBLEM REQUIRES IGNORING NEWLINES, ALTHOUGH THE INPUT IS SPLIT OVER SEVERAL LINES THIS SHOULD BE IGNORED
input = open('input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().splitlines()

def stripdonts(line):
    result = ''
    endpos = 0
    startpos = line.find(r"don't()")
    if (startpos == -1):
        return(line)
    while (startpos != -1):
        result += line[endpos:startpos-1]
        endpos = line.find(r"do()", startpos+6)
        if endpos != -1:
            endpos += 4
            startpos = line.find(r"don't()", endpos)
            if (startpos == -1):
                result += line[endpos:]
        else:
            break
    return result


def solve1():
    result = 0
    for line in input:
        #muls = re.findall("mul[(][0-9]{1,3},[0-9]{1,3}[)]", line)
        results = [int(x)*int(y) for x,y in re.findall("mul[(]([0-9]{1,3}),([0-9]{1,3})[)]", line)]
        result += sum(results)
        #print(muls)
        #print(results)
            
    print("Deel 1: " + str(result))

def solve2():
    result = 0
    for x,line in enumerate(input):
        print(x)
        ### USE re.DOTALL AS A FLAG FOR THE REGULAR EXPRESSION TO PROCESS NEWLINES
#        activemuls = re.findall(r"do\(\)(.*?)don't\(\)", 'do()'+line+"don't()")
#        activemuls = re.sub(r"don't\(\).*?do\(\)", '', line)
        activemuls = stripdonts(line)
        print(activemuls)
        results = [int(x)*int(y) for x,y in re.findall("mul[(]([0-9]{1,3}),([0-9]{1,3})[)]", activemuls)] #''.join(activemuls))]
        result += sum(results)
    print("Deel 2: " + str(result))

start = datetime.datetime.now()
solve1()
print("Tijd voor oplossing 1: ", datetime.datetime.now()-start)

start = datetime.datetime.now()
solve2()
print("Tijd voor oplossing 2: ", datetime.datetime.now()-start)
