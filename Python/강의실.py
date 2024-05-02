import sys, heapq
input = sys.stdin.readline

N = int(input())
times = []
for _ in range(N):
    a, b, c = map(int, input().split())
    times.append([b, c])
heapq.heapify(times)

end_times = [heapq.heappop(times)[1]]
while times:
    s, e = heapq.heappop(times)
    min_end_time = heapq.heappop(end_times)
    if min_end_time > s:
        heapq.heappush(end_times, min_end_time) # restore
    heapq.heappush(end_times, e)

print(len(end_times))