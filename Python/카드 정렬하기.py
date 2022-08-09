import heapq

N = int(input())
heap=[]

for _ in range(N): heapq.heappush(heap, int(input()))

RET=0

while len(heap)>=2:
    a1=heapq.heappop(heap)
    a2=heapq.heappop(heap)
    RET+=a1+a2
    heapq.heappush(heap, a1+a2)
print(RET)