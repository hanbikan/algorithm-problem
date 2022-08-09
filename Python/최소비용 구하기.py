import sys
import heapq
input = sys.stdin.readline


def getMinTime(start, end):
    todo = [(start, 0)]
    dist = [float('inf')]*(N+1)
    dist[start] = 0

    while todo:
        curNode, curDist = heapq.heappop(todo)

        if curDist > dist[curNode]:
            continue

        for n, d in graph[curNode]:
            nextDist = curDist + d
            if dist[n] > nextDist:
                dist[n] = nextDist
                heapq.heappush(todo, (n, nextDist))

    return dist[end]


if __name__ == '__main__':
    N = int(input())
    M = int(input())

    graph = {i: [] for i in range(1, N+1)}
    for _ in range(M):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))

    start, end = map(int, input().split())

    minTime = getMinTime(start, end)
    print(minTime)
