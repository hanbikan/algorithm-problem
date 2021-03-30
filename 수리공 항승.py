import sys
input = sys.stdin.readline

N, L = map(int, input().split())
leaks = list(map(int, input().split()))
leaks.sort()

cntTape = 0
noLeakUntil = 0
for leak in leaks:
    if noLeakUntil < leak:
        noLeakUntil = leak + L - 1
        cntTape += 1

print(cntTape)
