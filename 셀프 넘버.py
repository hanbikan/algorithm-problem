def d(n):
    RET = n
    for c in str(n):
        RET += int(c)
    return RET


isSelfNumberList = [True]*10001

for i in range(10000):
    curD = d(i)
    if curD <= 10000:
        isSelfNumberList[curD] = False

for i in range(10000):
    if isSelfNumberList[i]:
        print(i)
