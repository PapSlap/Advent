# Day 6 Part 1
file = open(r'C:\Users\Trevor\Desktop\Python Projects\Advent\day6data.txt')
data = file.read().split('\n')

l = len(data)
'''
Organize data into lists of groups
'''
grp = []
grps = []
for x in range(l):
    if data[x] is not "":
        grp.append(data[x])
    if data[x] is "":
        grps.append(grp)
        grp = []


'''
Count each letter once when it appears in a group
'''
l2 = len(grps)
import numpy as np


totalcount = np.array([0] * 26)
lettercount = np.array([0] * 26)
for x in range(l2):
    group = grps[x]
    for y in range(len(group)):
        pers = group[y]
        for z in range(len(pers)):
            index = ord(pers[z]) - 97
            if lettercount[index] == 0:
                lettercount[index] = 1
    totalcount = np.add(totalcount, lettercount)
    lettercount = np.array([0] * 26)

print(np.sum(totalcount))

# Part Two
tot = 0
totalcount = np.array([0] * 26)
lettercount = np.array([0] * 26)
for x in range(l2):
    group = grps[x]
    #print(group)
    for y in range(len(group)):
        pers = group[y]
        for z in range(len(pers)):
            index = ord(pers[z]) - 97
            lettercount[index] += 1
    for t in range(26):
        if lettercount[t] == len(group):
            tot += 1
    lettercount = np.array([0] * 26)
print(tot)