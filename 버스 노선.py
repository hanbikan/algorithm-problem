import sys
input = sys.stdin.readline


def getIsRemainer(info):
    info.sort(reverse=True, key=lambda x: x[1])
    info.sort(key=lambda x: x[0])

    isRemainer = [True for i in range(M)]
    maxB = 0
    for a, b, c in info:
        if maxB < b:
            maxB = b
        else:
            isRemainer[c-1] = False

    return isRemainer


def printIsRemainer(isRemainer):
    curRoute = 1
    for b in isRemainer:
        if b:
            print(curRoute, end=" ")
        curRoute += 1


if __name__ == '__main__':
    N = int(input())
    M = int(input())

    info = []
    for i in range(M):
        a, b = map(int, input().split())
        if a < b:
            info += [(a, b, i+1), (a+N, b+N, i+1)]
        else:
            info.append((a, b+N, i+1))

    isRemainer = getIsRemainer(info)
    printIsRemainer(isRemainer)
