from queue import PriorityQueue
import sys
input = sys.stdin.readline

def get_min_dist():
    dists = [float('inf')] * 10001
    q = PriorityQueue()
    q.put([0, 0])
    dists[0] = 0

    while not q.empty():
        cur_dist, cur_node = q.get()
        if cur_node == D:
            return dists[D]
        
        for next_dist, next_node in graph[cur_node]:
            if cur_dist + next_dist < dists[next_node]:
                q.put([cur_dist + next_dist, next_node])
                dists[next_node] = cur_dist + next_dist
    
    return 0

N, D = map(int, input().split())
nodes = set()
graph = {i: [] for i in range(10001)}
for _ in range(N):
    a, b, c = map(int, input().split())
    if a > D or b > D: continue

    graph[a].append([c, b])
    nodes.add(a)
    nodes.add(b)

nodes.add(0)
nodes.add(D)
nodes = sorted(list(nodes))

for i in range(len(nodes)):
    for j in range(i + 1, len(nodes)):
        a, b = nodes[i], nodes[j]
        graph[a].append([b - a, b])
            
print(get_min_dist())