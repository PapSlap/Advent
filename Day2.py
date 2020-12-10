# Open Text File, read and save data
file = open(r'C:\Users\Trevor\Desktop\Python Projects\Advent\day2data.txt')
data = file.read()
data = [str(i) for i in data.split()]

l = len(data)
col = int(3)
row = int(l/3)
array = [[0 for x in range(row)] for x in range(col)]

i = 0
j = 0
k = 0
while i < row:
    j = 0
    while j < col:
        array[j][i] = data[k]
        k = k + 1
        j = j + 1
    i = i + 1

i = 0
correct = 0
while i < row:
    num = array[0][i].split('-')
    lett = str(array[1][i].split(':')[0])
    pw = str(array[2][i])
    ll = int(num[0])
    ul = int(num[1])
    cnt = pw.count(lett)
    if cnt >= ll and cnt <= ul:
        correct = correct + 1
    i = i + 1

print('Part one correct passwords: ' + str(correct))


# Part two

i = 0
correct2 = 0
while i < row:
    num = array[0][i].split('-')
    lett = str(array[1][i].split(':')[0])
    pw = str(array[2][i])
    ll = int(num[0]) - 1
    ul = int(num[1]) - 1 
    lpw = len(pw)
    if ul <= lpw:
        if bool(pw[ll] == lett) ^ bool(pw[ul] == lett):
            correct2 = correct2 + 1
    i = i + 1

print('Part two correct passwords: ' + str(correct2))