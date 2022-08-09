import sys
input = sys.stdin.readline


def setJumpCounts(maxIndex):
    global jumpCounts
    lastIndex = 1
    i = 2

    while lastIndex < maxIndex:
        rep = (i+1)//2
        jumpCounts.append(jumpCounts[i-1]+rep)

        lastIndex = jumpCounts[-1]
        i += 1


# [0,1,2,4,6]에서 4의 의미: 거리의 차이가 4인 곳까지의 점프 횟수가 해당 index인 3이다.
# 1 2 3 4 5 6 (인덱스)
# 1 2 3 3 4 4 (값)
jumpCounts = [0, 1]

T = int(input())
diffs = []

for _ in range(T):
    x, y = map(int, input().split())
    diffs.append(y-x)

setJumpCounts(max(diffs))
print(jumpCounts)
for i in range(T):
    for j in range(len(jumpCounts)-1, 0, -1):
        if jumpCounts[j-1] < diffs[i] <= jumpCounts[j]:
            print(j)
            break
