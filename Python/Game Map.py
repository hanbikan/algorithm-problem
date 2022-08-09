import sys
input = sys.stdin.readline
COUNT, NEIGHBOR = 0, 1

def f(node):
    res = 0

    for next in graph[node][NEIGHBOR]:
        if dp[next] == -1: f(next)
        res = max(res, dp[next])

    dp[node] = 1 + res

if __name__ == '__main__':
    n, m = map(int,input().split())
    graph = {i:[0, []] for i in range(n)}
    
    inputs = [list(map(int,input().split())) for _ in range(m)]
    for i in range(m):
        i, j = inputs[i]
        graph[i][COUNT] += 1
        graph[j][COUNT] += 1
        
    for i in range(m):
        i, j = inputs[i]
        if graph[i][COUNT] < graph[j][COUNT]:
            graph[i][NEIGHBOR].append(j)
        if graph[j][COUNT] < graph[i][COUNT]:
            graph[j][NEIGHBOR].append(i)

    res = 0
    dp = [-1]*n
    for i in range(n):
        if dp[i] == -1: f(i)
        res = max(res, dp[i])
    print(res)