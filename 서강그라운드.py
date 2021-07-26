import sys
import heapq
input = sys.stdin.readline


def getPossibleItemCount(start):
    dp = [float('inf')]*(n+1)
    dp[start] = 0
    todo = [(0, start)]

    while todo:
        curDist, curNode = heapq.heappop(todo)

        if curDist > dp[curNode]:
            continue

        for next, dist in graph[curNode]:
            nextDist = curDist + dist

            if nextDist <= m and nextDist < dp[next]:
                dp[next] = nextDist
                heapq.heappush(todo, (nextDist, next))

    possibleItemCount = 0

    for i in range(1, n+1):
        if dp[i] != float('inf'):
            possibleItemCount += itemCounts[i]

    return possibleItemCount


if __name__ == '__main__':
    # 입력
    n, m, r = map(int, input().split())
    itemCounts = [-1] + list(map(int, input().split()))

    graph = [[] for _ in range(n+1)]
    for _ in range(r):
        a, b, l = map(int, input().split())
        graph[a].append((b, l))
        graph[b].append((a, l))

    # 처리
    maxItemCount = 0
    for i in range(1, n+1):
        maxItemCount = max(maxItemCount, getPossibleItemCount(i))

    # 출력
    print(maxItemCount)
