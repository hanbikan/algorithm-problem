def checkIsHansu(num):
    strNum = str(num)
    if len(strNum) >= 3:
        lastDiff = int(strNum[1]) - int(strNum[0])
        for i in range(1, len(strNum)-1):
            if int(strNum[i+1]) - int(strNum[i]) != lastDiff:
                return False
            lastDiff = int(strNum[i+1]) - int(strNum[i])

    return True


hansuCount = 0
X = int(input())
for i in range(1, X+1):
    if checkIsHansu(i):
        hansuCount += 1

print(hansuCount)
