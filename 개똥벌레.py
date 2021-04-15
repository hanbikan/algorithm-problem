import sys
input = sys.stdin.readline

N, H = map(int, input().split())
bottomObstacles = [0]*H
topObstacles = [0]*H

for i in range(N//2):
    o1, o2 = int(input()), int(input())
    bottomObstacles[o1-1] += 1
    topObstacles[o2-1] += 1

bottomPrefixSum = [0]*(H+1)
topPrefixSum = [0]*(H+1)
for i in range(H-1, -1, -1):
    bottomPrefixSum[i] = bottomPrefixSum[i+1] + bottomObstacles[i]
    topPrefixSum[i] = topPrefixSum[i+1] + topObstacles[i]

minObstaclesToBeDestroyed, minCount = 400001, 0
for b, t in zip(range(H), range(H-1, -1, -1)):
    cur = bottomPrefixSum[b] + topPrefixSum[t]

    if cur == minObstaclesToBeDestroyed:
        minCount += 1
    elif cur < minObstaclesToBeDestroyed:
        minObstaclesToBeDestroyed = cur
        minCount = 1

print(minObstaclesToBeDestroyed, minCount)
