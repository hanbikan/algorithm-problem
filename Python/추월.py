import sys
input = sys.stdin.readline

N = int(input())
cars1 = [str(input().rstrip()) for _ in range(N)]
cars2 = [str(input().rstrip()) for _ in range(N)]

i = 0
j = 0
overtaked = set()
while (i < N):
    if cars1[i] in overtaked:
        i += 1
        continue

    found = cars2.index(cars1[i], j)
    for k in range(j, found):
        overtaked.add(cars2[k])

    j = found + 1
    i += 1

print(len(overtaked))