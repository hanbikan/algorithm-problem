import sys
input = sys.stdin.readline

N = int(input())
distances = list(map(int, input().split()))
prices = list(map(int, input().split()))

curMin = prices[0]
minCost = 0

for i in range(N-1):
    curMin = min(curMin, prices[i])
    minCost += curMin*distances[i]

print(minCost)
