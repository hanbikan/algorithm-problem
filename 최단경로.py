import sys
import heapq
input = sys.stdin.readline


def bfs(start):
    global minWeights
    minWeights[start] = 0

    heap = []
    heapq.heappush(heap, (0, start))

    while heap:
        curWeight, curNode = heapq.heappop(heap)

        for adjacentNode, adjacentWeight in graph[curNode].items():
            nextAdjacentWeight = curWeight + adjacentWeight

            # 처음 방문이거나, 이미 방문하였으나 더 짧은 경로일 때
            if minWeights[adjacentNode] == -1 or minWeights[adjacentNode] > nextAdjacentWeight:
                minWeights[adjacentNode] = nextAdjacentWeight
                heapq.heappush(heap, (nextAdjacentWeight, adjacentNode))


# Input
V, E = map(int, input().split())
graph = {i: {} for i in range(1, V+1)}

K = int(input())
for _ in range(E):
    u, v, w = map(int, input().split())
    # u에서 v로 갈 때의 비용을 최소값으로 유지시킴
    graph[u][v] = min(graph[u][v], w) if graph[u].get(v) else w

# Solution
minWeights = [-1 for i in range(V+1)]
bfs(K)

for i in range(1, V+1):
    print(minWeights[i] if minWeights[i] != -1 else "INF")
