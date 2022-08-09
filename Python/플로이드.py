import sys
input = sys.stdin.readline
INF = 100001


def floydWarshall(n):
    dp = [[INF*100]*(n+1) for _ in range(n+1)]

    # 초기화
    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][j] != INF:
                dp[i][j] = graph[i][j]

    # 플로이드
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if dp[i][k] + dp[k][j] < dp[i][j]:
                    dp[i][j] = dp[i][k] + dp[k][j]

    # 출력
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j or dp[i][j] == INF*100:
                print(0, end=" ")
            else:
                print(dp[i][j], end=" ")
        print()


if __name__ == '__main__':
    n = int(input())
    m = int(input())

    graph = [[INF]*(n+1) for _ in range(n+1)]

    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a][b] = min(graph[a][b], c)

    floydWarshall(n)
