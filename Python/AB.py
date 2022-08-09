import sys
input = sys.stdin.readline


def getStr(N, K):
    curStr = ['B']*N
    aCount = 0
    curK = 0
    lastAIndex = -1

    while curK < K:
        if lastAIndex <= aCount-1:
            if curStr[N-1-(aCount+1)] == 'A':
                break
            else:
                curStr[N-1-(aCount+1)] = 'A'
                lastAIndex = N-1-(aCount+1)
                aCount += 1
                curK += 1
        else:
            curStr[lastAIndex] = 'B'
            curStr[lastAIndex-1] = 'A'
            lastAIndex -= 1
            curK += 1

    if curK == K:
        return curStr
    else:
        return "-1"


N, K = map(int, input().split())
print("".join(getStr(N, K)))
