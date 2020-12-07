# Day 5 Part 1
file = open(r'C:\Users\Trevor\Desktop\Python Projects\Advent\day5data.txt')
data = file.read()
data = [str(i) for i in data.split()]

l = len(data)

def seatid(char,row1,row2):
    num = row2 - row1 + 1
    if char == "F" or char == 'L':
        row2 -= ((num/2))
    if char == "B" or char == 'R':
        row1 += (num/2)
    return [row1,row2]


rows = []
col = []
id = []
for x in range(l):
    bpass = data[x]
    row1 = 0
    row2 = 127
    for y in range(7):
        temprow = seatid(bpass[y],row1,row2)
        row1 = temprow[0]
        row2 = temprow[1]
    col1 = 0
    col2 = 7
    for y in range(7,10):
        tempcol = seatid(bpass[y],col1,col2)
        col1 = tempcol[0]
        col2 = tempcol[1]
    rows.append(row1)
    col.append(col1)
    id.append((row1 * 8) + col1)

print(f'Max id is: {max(id)}')

# Part 2

for x in range(71,len(id)):
    if float(x) not in id:
        print(f'My Seat Id: {x}')