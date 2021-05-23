import sys
input = sys.stdin.readline


def getRetangularArea(index):
    global todo
    left = right = index

    while 0 <= left:
        if curNums[left] < curNums[index]:
            break
        elif curNums[left] == curNums[index]:
            todo[left] = False
        left -= 1
    left += 1

    while right <= curLen-1:
        if curNums[right] < curNums[index]:
            break
        elif curNums[right] == curNums[index]:
            todo[right] = False
        right += 1
    right -= 1

    return ((right - left) + 1)*curNums[index]


while True:
    curNums = list(map(int, input().split()))
    if curNums == [0]:
        break

    curLen = curNums.pop(0)

    todo = [True for _ in range(curLen)]
    maxRetangularArea = 0

    for i in range(curLen):
        if todo[i]:
            maxRetangularArea = max(maxRetangularArea, getRetangularArea(i))

    print(maxRetangularArea)
