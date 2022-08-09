import sys
import heapq
input = sys.stdin.readline


def getMinCostAndPath(start, end):
    dp = [float('inf') for _ in range(n+1)]
    todo = [(0, start, [start])]

    while todo:
        curCost, curNode, curPath = heapq.heappop(todo)

        # 우선순위큐로 꺼내므로 최소 비용이 드는 루트를 가장 먼저 방문함
        if curNode == end:
            return curCost, curPath

        if dp[curNode] < curCost:
            continue

        for adjNode, adjCost in graph[curNode]:
            nextCost = curCost + adjCost

            if nextCost < dp[adjNode]:
                dp[adjNode] = nextCost
                heapq.heappush(todo, (nextCost, adjNode, curPath + [adjNode]))


if __name__ == '__main__':
    n = int(input())
    m = int(input())

    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        s, e, c = map(int, input().split())
        graph[s].append((e, c))

    start, end = map(int, input().split())
    minCost, path = getMinCostAndPath(start, end)

    print(minCost)
    print(len(path))
    print(*path)
