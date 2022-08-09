import sys
input = sys.stdin.readline


def getIsPrimeNumberList(N):
    isPrimeNumberList = [True]*(N+1)
    isPrimeNumberList[1] = False

    for i in range(2, int(N**(1/2))+1):
        if isPrimeNumberList[i]:
            j = 2
            while i*j <= N:
                isPrimeNumberList[i*j] = False
                j += 1

    return isPrimeNumberList


M, N = map(int, input().split())
isPrimeNumberList = getIsPrimeNumberList(N)
for i in range(M, N+1):
    if isPrimeNumberList[i]:
        print(i)
