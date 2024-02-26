import sys
input = sys.stdin.readline

def f(strr):
    if length <= 3:
        if length == 3:
            return strr[0] == strr[2]
        elif length == 2:
            return strr[0] == strr[1]
        else:
            return True

    # get units(min: 2 or 3)
    units = []
    contains_one_space = []
    cur = length
    while cur // 2 >= 3:
        next_cur = cur // 2
        units.append(next_cur)
        contains_one_space.append(cur % 2 == 1)
        cur = next_cur
    units = units[::-1]
    contains_one_space = contains_one_space[::-1]

    if (units[0] == 3 and strr[0] != strr[2]):
        return False
    elif (units[0] == 2 and strr[0] != strr[1]):
        return False

    for d in range(len(units)):
        unit, contains = units[d], contains_one_space[d]
        for i in range(unit):
            if strr[i] != strr[i + unit + contains]:
                return False
    
    return True

strr = input().rstrip()
length = len(strr)

if (f(strr)):
    print("AKARAKA")
else:
    print("IPSELENTI")