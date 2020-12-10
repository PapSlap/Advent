# Day 7 Part 1
file = open(r'C:\Users\Trevor\Desktop\Python Projects\Advent\day7data.txt')
data = file.read().split('\n')

l = len(data)

'''
Organize data into bigbag list and smallbag list
'''
bigbag = []
smallbag = []
for x in range(l):
    split1 = data[x].split(' contain ')
    split2 = split1[0].split(' bags')
    bigbag.append(split2[0])
    smallbag.append(split1[1])

'''
Function to find indices of 'find' string in 'findlist' list
'''
def findindex(find,findlist):
    foundlist = [i for i, j in enumerate(findlist) if find in j]
    return foundlist

'''
Find bags that can hold shiny gold bags
'''
holdgold = findindex('shiny gold',smallbag)

'''
Find bags that hold bags that hold shiny gold bags, only save their index if it isn't listed already
'''
for x in holdgold:
    input = bigbag[x]
    found = (findindex(input,smallbag))
    l2 = len(found)
    for y in range(l2): 
            if found[y] not in holdgold:
                holdgold.append(found[y])

gold = len(holdgold)
print(gold)

# Day 7 Part 2

goldindex = findindex('shiny gold',bigbag)
goldindex = goldindex[0]

def formatbags(rawbag):
    form1 = rawbag.split(' ')
    form2 = []
    form3 = []
    for x in range(len(form1)):
        if (x%4) == 0:
            form2.append(form1[x])
        if (x - 1)%4 == 0:
            form3.append(form1[x] + ' ' + form1[x+1])
    return [form2, form3]

goldstart = smallbag[goldindex]
bags = formatbags(goldstart)

total = 0
nums = bags[0]
colors = bags[1]
number = 0
for x in colors:
    number = int(nums[colors.index(x)])
    total += number
    find = (findindex(x,bigbag))[0]
    nextbag = formatbags(smallbag[find])
    newnum1 = nextbag[0]
    newcol1 = nextbag[1]
    if newnum1 != ["no"]:
        for y in newcol1:
            number1 = number * int(newnum1[newcol1.index(y)])
            total += number1
            find = (findindex(y,bigbag))[0]
            nextbag = formatbags(smallbag[find])
            newnum2 = nextbag[0]
            newcol2 = nextbag[1]
            if newnum2 != ["no"]:
                for z in newcol2:
                    number2 = number1 * int(newnum2[newcol2.index(z)])
                    total += number2
                    find = (findindex(z,bigbag))[0]
                    nextbag = formatbags(smallbag[find])
                    newnum3 = nextbag[0]
                    newcol3 = nextbag[1]
                    if newnum3 != ["no"]:
                        for w in newcol3:
                            number3 = number2 * int(newnum3[newcol3.index(w)])
                            total += number3
                            find = (findindex(w,bigbag))[0]
                            nextbag = formatbags(smallbag[find])
                            newnum4 = nextbag[0]
                            newcol4 = nextbag[1]
                            if newnum4 != ["no"]:
                                for a in newcol4:
                                    number4 = number3 * int(newnum4[newcol4.index(a)])
                                    total += number4
                                    find = (findindex(a,bigbag))[0]
                                    nextbag = formatbags(smallbag[find])
                                    newnum5 = nextbag[0]
                                    newcol5 = nextbag[1]
                                    if newnum5 != ["no"]:
                                        for b in newcol5:
                                            number5 = number4 * int(newnum5[newcol5.index(b)])
                                            total += number5
                                            find = (findindex(b,bigbag))[0]
                                            nextbag = formatbags(smallbag[find])
                                            newnum6 = nextbag[0]
                                            newcol6 = nextbag[1]
                                            if newnum6 != ["no"]:
                                                for c in newcol6:
                                                    number6 = number5 * int(newnum6[newcol6.index(c)])
                                                    total += number6
                                                    find = (findindex(c,bigbag))[0]
                                                    nextbag = formatbags(smallbag[find])
                                                    newnum7 = nextbag[0]
                                                    newcol7 = nextbag[1]
                                                    if newnum7 != ["no"]:
                                                                print('******************************************************************************still going')

print(total)