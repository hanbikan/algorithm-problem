import sys


def getMaxVisitable(N, M):
    if N == 1:
        return 1
    elif N == 2:
        return min(4, (M+1)//2)
    elif N >= 3:
        if M >= 7:
            return M-2
        else:
            return min(M, 4)


input = sys.stdin.readline
N, M = map(int, input().split())

print(getMaxVisitable(N, M))
