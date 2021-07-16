import sys
import heapq
input = sys.stdin.readline


def djikstra(start):
    dp = {i: float('inf') for i in range(1, N + 1)}
    dp[start] = 0
    todo = [(start, 0)]

    while todo:
        curNode, curDist = heapq.heappop(todo)

        if dp[curNode] < curDist:
            continue

        for b, c in graph[curNode]:
            nextDist = curDist + c

            if dp[b] > nextDist:
                dp[b] = nextDist
                heapq.heappush(todo, (b, nextDist))

    return dp


if __name__ == '__main__':
    N, E = map(int, input().split())

    graph = {i: [] for i in range(1, N + 1)}
    for _ in range(E):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))

    v1, v2 = map(int, input().split())

    dp1 = djikstra(v1)
    dp2 = djikstra(v2)

    sum1 = dp1[1] + dp1[v2] + dp2[N]
    sum2 = dp2[1] + dp2[v1] + dp1[N]

    if sum1 == float('inf') and sum2 == float('inf'):
        print(-1)
    else:
        print(min(sum1, sum2))
