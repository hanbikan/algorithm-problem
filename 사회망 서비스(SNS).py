import sys

sys.setrecursionlimit(300000)
input = sys.stdin.readline
TRUE, FALSE = 1, 0
INF = 1000001


def dfs(is_early_adapter, node, prev):
    # If dp already exists
    if dp[is_early_adapter][node] != INF:
        return

    adapter_count = is_early_adapter

    if is_early_adapter == TRUE:
        for n in graph[node]:
            if n == prev:
                continue

            dfs(TRUE, n, node)
            dfs(FALSE, n, node)

            adapter_count += min(dp[TRUE][n], dp[FALSE][n])

    else:
        for n in graph[node]:
            if n == prev:
                continue

            dfs(TRUE, n, node)

            adapter_count += dp[TRUE][n]

    dp[is_early_adapter][node] = adapter_count


if __name__ == '__main__':
    # Input
    N = int(input())
    graph = [[] for _ in range(N+1)]
    for _ in range(N-1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    # Add root
    graph[0].append(1)

    # Set dp
    dp = [[INF]*(N+1) for _ in range(2)]
    dfs(TRUE, 0, 0)

    # Print result
    print(dp[1][0] - 1)
