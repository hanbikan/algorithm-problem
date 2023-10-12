import sys
input = sys.stdin.readline

# Input
n, k = map(int,input().split())
graph = {i: [] for i in range(n)}
for _ in range(n - 1):
    p, c = map(int,input().split())
    graph[p].append(c)
apple_counts = list(map(int,input().split()))

# BFS
q = [0]
apple_count = apple_counts[0]
current_distance = 0
while current_distance <= k - 1 and len(q) > 0:
    nq = []
    while len(q) > 0:
        current_node = q.pop(0)
        for next_node in graph[current_node]:
            nq.append(next_node)
            apple_count += apple_counts[next_node]
    current_distance += 1
    q = nq

print(apple_count)