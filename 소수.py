import sys
input = sys.stdin.readline


def isPrimeNumber(n):
    for i in range(2, int(n**(1/2))+1):
        if n % i == 0:
            return False
    return True


M = int(input())
N = int(input())

isPrimeNumberList = [True]*(N+1)

primeMin = 10001
primeSum = 0

for i in range(2, N+1):
    if isPrimeNumberList[i]:
        if not isPrimeNumber(i):
            isPrimeNumberList[i] = False
            continue

        isPrimeNumberList[i] = True

        if i >= M:
            primeSum += i
            primeMin = min(primeMin, i)

        j = 2
        while i*j < N+1:
            isPrimeNumberList[i*j] = False
            j += 1

if primeMin == 10001 and primeSum == 0:
    print(-1)
else:
    print(primeSum)
    print(primeMin)
