import sys
input = sys.stdin.readline


N = int(input())
postOffice = [list(map(int, input().split())) for _ in range(N)]

postOffice.sort(key=lambda x: x[0])
mid = round(sum(p for _, p in postOffice)/2)

pCount = 0
for i, p in postOffice:
    pCount += p

    if pCount >= mid:
        print(i)
        break
