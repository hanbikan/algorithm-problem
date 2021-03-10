import heapq
import sys
input = sys.stdin.readline

N = int(input())
S, T = 0, 1  # define
times = []
for _ in range(N):
    times.append(list(map(int, input().split())))
times.sort(key=lambda x: x[0])

queue = []
heapq.heappush(queue, times[0][T])

for i in range(1, N):
    if times[i][S] >= queue[0]:
        heapq.heappop(queue)
        heapq.heappush(queue, times[i][T])
    else:
        heapq.heappush(queue, times[i][T])

print(len(queue))
