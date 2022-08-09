import sys
input = sys.stdin.readline
INF = 100*1000+1


def dijkstra(start, graph):
    dp = [INF]*(N+1)
    dp[start] = 0
    todo = [(start, 0)]

    while todo:
        curNode, curTime = todo.pop(0)

        if curTime > dp[curNode]:
            continue

        for e, t in graph[curNode]:
            nextTime = curTime + t

            if nextTime < dp[e]:
                dp[e] = nextTime
                todo.append((e, nextTime))

    return dp


if __name__ == '__main__':
    # 입력
    N, M, X = map(int, input().split())

    g1 = [[] for _ in range(N+1)]
    g2 = [[] for _ in range(N+1)]

    for _ in range(M):
        s, e, t = map(int, input().split())
        g1[s].append((e, t))
        g2[e].append((s, t))

    # 다익스트라
    dp1 = dijkstra(X, g1)
    dp2 = dijkstra(X, g2)

    # 출력
    maxTime = max([dp1[i] + dp2[i] for i in range(1, N+1)])
    print(maxTime)
