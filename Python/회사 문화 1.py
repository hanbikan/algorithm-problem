from collections import deque
import sys
input = sys.stdin.readline


n, m = map(int, input().split())

parents = [-1] + list(map(int,input().split()))
graph = {i: [] for i in range(1, n+1)}
for i in range(2, n+1):
    graph[parents[i]].append(i)

weights = [0]*(n + 1)
for _ in range(m):
    i, w = map(int,input().split())
    weights[i] += w

results = [0]*(n+1)

q = deque([[1, 0]])
while len(q) > 0:
    i, w = q.popleft()
    for n in graph[i]:
        next_weight = w + weights[n]
        q.append([n, next_weight])
        results[n] = next_weight

print(*results[1:])