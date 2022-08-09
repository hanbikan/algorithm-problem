import sys
input = sys.stdin.readline


def convertMatrix(x, y):
    if not (0 <= x <= N-3 and 0 <= y <= M-3):
        return -1

    global matrixA

    for i in range(3):
        for j in range(3):
            matrixA[x+i][y+j] = not matrixA[x+i][y+j]

    return 0


def isDone():
    for i in range(N):
        for j in range(M):
            if matrixA[i][j] == True:
                return -1

    return 0


def printMatrix():
    for i in range(N):
        print(matrixA[i])


N, M = map(int, input().split())

matrixA = []
for _ in range(N):
    curList = []
    curLine = input().rstrip()
    for c in curLine:
        curList.append(int(c))
    matrixA.append(curList)

for i in range(N):
    curList = []
    curLine = input().rstrip()
    for j in range(M):
        if int(curLine[j]) == matrixA[i][j]:
            matrixA[i][j] = False
        else:
            matrixA[i][j] = True

conversionCount = 0
for i in range(N-2):
    for j in range(M-2):
        if matrixA[i][j] == True:
            if convertMatrix(i, j) == 0:
                conversionCount += 1

if isDone() == 0:
    print(conversionCount)
else:
    print(-1)
