import sys, collections
input = sys.stdin.readline

def find_farthest(node):
    q = collections.deque([(counts[node], node)])
    dists = [float('inf')] * (N + 1)
    dists[node] = counts[node]

    while q:
        dist, node = q.popleft()
        for next_node in graph[node]:
            next_dist = dist + counts[next_node]
            if next_dist < dists[next_node]:
                dists[next_node] = next_dist
                q.append((dist + counts[next_node], next_node))

    # find max dist
    max_dist = -1
    for dist in dists:
        if dist == float('inf'):
            continue
        max_dist = max(max_dist, dist)

    # find max dist nodes
    max_dist_nodes = []
    for i in range(1, N + 1):
        if dists[i] == max_dist:
            max_dist_nodes.append(i)

    return max_dist, max_dist_nodes

N = int(input())
counts = [0] + list(map(int, input().split()))
graph = {i: [] for i in range(1, N + 1)}
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

_, nodes = find_farthest(1)
start_node = nodes[0]
max_dist, max_dist_nodes = find_farthest(start_node)
print(max_dist, min(start_node, max_dist_nodes[0]))