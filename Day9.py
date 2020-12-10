# Day 9 Part 1
file = open(r'C:\Users\Trevor\Desktop\Python Projects\Advent\day9data.txt')
data = file.read().split('\n')
for x in range(len(data)):
    data[x] = int(data[x])

from itertools import combinations, chain, product

'''
Function that will return the summed combination of a list of numbers
nums = list of numbers        r = numbers per combination
numchecks([1,2,3],2) -> [3,4,4]
'''
def combos(nums, r):
    output = sum([list(map(list, (combinations(nums, r))))], [])
    for x in range(len(output)):
        output[x] = sum(output[x])
    return output

'''
Function to look that takes the index of a number in a list, and prints that number if
no combined sum of the number in range(index2,index3) equal that number
'''
def xmas(index1, index2, index3):
    number = data[index1]
    preamble = data[index2:index3]
    checks = combos(preamble,2)
    if number not in checks:
        return number

l = len(data)
for x in range(25,l):
    start = x - 25
    stop = x
    if xmas(x, start, stop) is not None: answer = xmas(x, start, stop)

# Day 8 Part 2
print(answer)

'''
Find consecutive list of numbers that add up to answer from part 1. Start at index 0, keep adding numbers if your 
total is not greater than answer. If total is greater than answer, go to index 1 and start over.
'''
start = 0
stop = 1
total = 0
while total != answer:
    total = sum(data[start:stop])
    if total < answer:
        stop += 1
    if total > answer:
        start += 1
        stop = start + 1
    if total == answer:
        low = min(data[start:stop])
        high = max(data[start:stop])
        answer2 = low + high
        print(answer2)