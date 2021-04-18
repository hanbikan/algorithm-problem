import heapq

N = int(input())

nums = []
for _ in range(N):
    heapq.heappush(nums, int(input()))

for _ in range(N):
    print(heapq.heappop(nums))
