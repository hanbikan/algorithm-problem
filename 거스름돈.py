def getChange(money, unit):
    return money//unit, money%unit

def solution():
    RET = 0
    UNITS = [500, 100, 50, 10, 5, 1]
    PAY = int(input())
    change = 1000-PAY
    for i in range(len(UNITS)):
        toAdd, change = getChange(change, UNITS[i])
        RET+=toAdd
    print(RET)

solution()