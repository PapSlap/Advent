# Day 11
file = open(r'C:\Users\Trevor\Desktop\Python Projects\Advent\day11data.txt')
data = file.read().split('\n')
for x in range(len(data)):
    data[x] = list(data[x])

lx = len(data) - 1
ly = len(data[0]) - 1

# Function to count adjacent cells of given x,y coordinates containing specific symbol
def countadj(x_cord,y_cord,symbol):
    count = 0
    for x,y in [(x_cord + i,y_cord + j) for i in (-1,0,1) for j in (-1,0,1) if i != 0 or j != 0]:
        if x >= 0 and x <= lx and y >= 0 and y <= ly:
            if data[x][y] == symbol:
                count += 1
    return count

# Create array the size of data set
countp = [[" " for x in range(ly + 1)] for x in range(lx + 1)]

# Keep itterating while changes are happening(itter2 is not itter1). Go through every x,y position in 
# dataset and count the # symbols in adjacent cells. If no seat is an L and no #s, change to #. If 
# seat is a # and more than 3 adjacent #s, change to L.
itter2 = 1
itter1 = 0
while itter2 != itter1: 
    for x in range(len(data)):
        for y in range(len(data[x])):
            countp[x][y] = countadj(x,y,'#')
    itter2 = itter1
    for x in range(len(data)):
        for y in range(len(data[x])):       
            if data[x][y] == 'L':
                if countp[x][y] == 0:
                    data[x][y] = '#'
                    itter2 += 1
            if data[x][y] == '#':
                if countp[x][y] >= 4:
                    data[x][y] = 'L'
                    itter2 += 1

# Count #s in dataset
occupied = 0
for x in range(len(data)):
    for y in range(len(data[x])):
        if data[x][y] == '#':
            occupied += 1
print(f'part one: {occupied}')

