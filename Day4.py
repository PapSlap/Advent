# Day 4 Part 1
file = open(r'C:\Users\Trevor\Desktop\Python Projects\Advent\day4data.txt').readlines()
#print(file)

l = len(file)
array = [[" " for x in range(8)] for x in range(l)]

i = 0
j = 0
user = 0
while i < l:
    if file[i] is "\n":
        user += 1
    else:
        data = file[i].split(" ")
        ld = len(data)
        j = 0
        while j < ld:
            if "byr:" in data[j]:
                data[j] = data[j].split(":")[1]
                data[j] = data[j].split("\n")[0]
                array[user][0] = data[j]
            if "iyr:" in data[j]:
                data[j] = data[j].split(":")[1]
                data[j] = data[j].split("\n")[0]
                array[user][1] = data[j]
            if "eyr:" in data[j]:
                data[j] = data[j].split(":")[1]
                data[j] = data[j].split("\n")[0]
                array[user][2] = data[j]
            if "hgt:" in data[j]:
                data[j] = data[j].split(":")[1]
                data[j] = data[j].split("\n")[0]
                array[user][3] = data[j]
            if "hcl:" in data[j]:
                data[j] = data[j].split(":")[1]
                data[j] = data[j].split("\n")[0]
                array[user][4] = data[j]
            if "ecl:" in data[j]:
                data[j] = data[j].split(":")[1]
                data[j] = data[j].split("\n")[0]
                array[user][5] = data[j]
            if "pid:" in data[j]:
                data[j] = data[j].split(":")[1]
                data[j] = data[j].split("\n")[0]
                array[user][6] = data[j]
            if "cid:" in data[j]:
                data[j] = data[j].split(":")[1]
                data[j] = data[j].split("\n")[0]
                array[user][7] = data[j]
            j += 1
    i += 1

print(f'total users: {user}')

i = 0
valid = 0
validindex = [0]
while i < user:
    if array[i][0] != " ":
        if array[i][1] != " ":
            if array[i][2] != " ":
                if array[i][3] != " ":
                    if array[i][4] != " ":
                        if array[i][5] != " ":
                            if array[i][6] != " ":
                                valid +=1
                                validindex.append(i)
    i += 1

print(validindex)

print(f'Valid users part one: {valid}')

i = 0
valid2 = 0
while i < user:
    if array[i][0] != " " and \
        int(array[i][0]) >= 1920 and int(array[i][0]) <= 2002:
        if array[i][1] != " " and \
            int(array[i][1]) >= 2010 and int(array[i][1]) <= 2020:
            if array[i][2] != " " and \
                int(array[i][2]) >= 2020 and int(array[i][2]) <= 2030:
                if array[i][3] != " ":
                    if "cm" in array[i][3]:
                        if (int(array[i][3].split("cm")[0]) >= 150 and int(array[i][3].split("cm")[0]) <= 193):
                            if array[i][4] != " ":
                                hcl = array[i][4]
                                allowed_chars = set('123456789abcdef')
                                l5 = len(hcl)
                                if hcl[0] == "#":
                                    if set(array[i][4].split('#')[1]).issubset(allowed_chars) and l5 == 7:
                                        if array[i][5] != " " and (array[i][5] == "amb" or array[i][5] == "blu" or \
                                            array[i][5] == "brn" or array[i][5] == "gry" or array[i][5] == "grn" or \
                                            array[i][5] == "hzl" or array[i][5] == "oth"):
                                            if array[i][6] != " ":
                                                allowed_chars = set('0123456789')
                                                if set(array[i][6]).issubset(allowed_chars) and len(array[i][6]) == 9:
                                                    valid2 +=1
                                                    print(array[i][0:7])
                    elif "in" in array[i][3]:
                        if (int(array[i][3].split("in")[0]) >= 59 and int(array[i][3].split("in")[0]) <= 76):
                            if array[i][4] != " ":
                                hcl = array[i][4]
                                allowed_chars = set('123456789abcdef')
                                l5 = len(hcl)
                                if hcl[0] == "#":
                                    if set(array[i][4].split('#')[1]).issubset(allowed_chars) and l5 == 7:
                                        if array[i][5] != " " and (array[i][5] == "amb" or array[i][5] == "blu" or \
                                            array[i][5] == "brn" or array[i][5] == "gry" or array[i][5] == "grn" or \
                                            array[i][5] == "hzl" or array[i][5] == "oth"):
                                            if array[i][6] != " ":
                                                allowed_chars = set('0123456789')
                                                if set(array[i][6]).issubset(allowed_chars) and len(array[i][6]) == 9:
                                                    valid2 +=1
                                                    print(array[i][0:7])
    i += 1

print(f'Valid users part two: {valid2}')