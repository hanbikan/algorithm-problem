from queue import PriorityQueue
import sys
input = sys.stdin.readline

def dijkstra():
    q = PriorityQueue()
    q.put([0, 0, 0]) # dist, node, is_very_lager_jump_used
    dists = [[float('inf')] * (N + 2) for _ in range(2)]
    dists[0][0] = 0

    while (not q.empty()):
        cur_dist, cur_node, is_very_lager_jump_used = q.get()
        for dist, next_node in graph[cur_node]:
            next_dist = cur_dist + dist
            if cur_node + 3 == next_node:
                if is_very_lager_jump_used == 1: continue
                else: is_very_lager_jump_used = 1
            if (next_dist < dists[is_very_lager_jump_used][next_node]):
                dists[is_very_lager_jump_used][next_node] = next_dist
                q.put([next_dist, next_node, is_very_lager_jump_used])
    
    return min(dists[0][N - 1], dists[1][N - 1])

N = int(input())
graph = {i:[] for i in range(N + 2)}
for i in range(N - 1):
    a, b = map(int,input().split())
    graph[i].append([a, i + 1])
    graph[i].append([b, i + 2])

K = int(input())
for i in range(N - 1):
    graph[i].append([K, i + 3])

print(dijkstra())