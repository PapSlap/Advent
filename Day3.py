# Day 3 Part 1
file = open(r'C:\Users\Trevor\Desktop\Python Projects\Advent\day3data.txt')
data = file.read()
data = [str(i) for i in data.split()]

l = len(data)

i = 0
j = 0
m = 0
n = 0
o = 0
p = 1
trees11 = 0
trees31 = 0
trees51 = 0
trees71 = 0
trees12 = 0

while i < l:
    print(i%2 != 0)
    row = data[i]
    l2 = len(data[i])
    if row[j] == '#':
        trees31 = trees31 + 1
    if (i % 2) == 0 and i != 0:
        if row[p] == '#':
            trees12 = trees12 + 1
        p = p + 1
        if p >= l2:
            p = p - l2
    if row[m] == '#':
        trees11 = trees11 + 1
    if row[n] == '#':
        trees51 = trees51 + 1
    if row[o] == '#':
        trees71 = trees71 + 1
    i = i + 1
    j = j + 3
    if j >= l2:
        j = j - l2
    m = m + 1
    if m >= l2:
        m = m - l2
    n = n + 5
    if n >= l2:
        n = n - l2
    o = o + 7
    if o >= l2:
        o = o - l2

print('We would hit ' + str(trees31) + ' trees on 3x1. Ouch.')
print('We would hit ' + str(trees11) + ' trees on 1x1. Ouch.')
print('We would hit ' + str(trees51) + ' trees on 5x1. Ouch.')
print('We would hit ' + str(trees71) + ' trees on 7x1. Ouch.')
print('We would hit ' + str(trees12) + ' trees on 1x2. Ouch.')

print(trees11 * trees31 * trees51 * trees71 * trees12)