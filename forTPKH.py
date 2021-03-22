def getNextPos(cnt):
    curTableX, curTableY = getTablePos(cnt)
    eachTableIndex = cnt-(curTableX*N*T+curTableY*N)-1
    return curTableX, curTableY, int(eachTableIndex//(N**0.5)), int(eachTableIndex % (N**0.5))


def getTablePos(cnt):
    RET_x = (cnt-1) // (T*N)
    RET_y = ((cnt-1) % (T*N))//N
    return RET_x, RET_y


T = 4
N = 4
for i in range(1, 65):
    print(getNextPos(i))
