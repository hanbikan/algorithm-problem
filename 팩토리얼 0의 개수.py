import sys
input = sys.stdin.readline

N = int(input())

factorial = 1
for i in range(2, N+1):
    factorial *= i

zeroCount = 0
factorialStr = str(factorial)
factorialStrLen = len(factorialStr)

for i in range(factorialStrLen-1, -1, -1):
    if factorialStr[i] == '0':
        zeroCount += 1
    else:
        break

print(zeroCount)
