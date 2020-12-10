# Day 8 Part 1
file = open(r'C:\Users\Trevor\Desktop\Python Projects\Advent\day8data.txt')
data = file.read().split('\n')

prog = []
for x in data:
    op = x.split(' ')[0]
    arg = int(x.split(' ')[1])
    prog.append([op,arg,0])

acc = 0
x = 0
step = prog[x]
while step[2] == 0:
    step[2] = 1
    if step[0] == 'acc':
        acc += step[1]
        x += 1
    if step[0] == 'jmp':
        x += step[1]
    if step[0] == 'nop':
        x += 1
    step = prog[x]

print(f'part 1: {acc}')

# Day 8 Part 2

x = 0
step = prog[x]
l = len(prog)

'''
Function to test code and run for 608 (length of code) iterations. If 
'''
def gameboy():
    acc = 0
    x = 0
    it = 0
    step = prog[x]
    while it < 608:
        if step[0] == 'acc':
            acc += step[1]
            x += 1
        if step[0] == 'jmp':
            x += step[1]
        if step[0] == 'nop':
            x += 1
        if x < l:
            step = prog[x]
        else: 
            it = 609
        it += 1
    return [acc, x]

'''
Change jmp and nop one by one into the other. Change back if desired effect isn't reached.
'''
for y in prog:
    if y[0] == 'jmp':
        y[0] = 'nop'
        test = gameboy()
        if test[1] >= l:
            ans = test[0]
        else:
            y[0] = 'jmp'
    if y[0] == 'nop':
        y[0] = 'jmp'
        test = gameboy()
        if test[1] >= l:
            ans = test[0]
        else:
            y[0] = 'nop'

print(f'part two: {ans}')