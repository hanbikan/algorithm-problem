import sys
input = sys.stdin.readline

def solution(n, s, a, b, fares):
    graph = {i: [] for i in range(1, n+1)}
    dist = [[float('inf')]*(n+1) for _ in range(n+1)]
    for fa, fb, fc in fares:
        graph[fa].append([fb, fc])
        graph[fb].append([fa, fc])
        dist[fa][fb] = fc
        dist[fb][fa] = fc
    for i in range(1, n+1):
        dist[i][i] = 0

    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
                
    # s -> m -> a, b
    res = float('inf')
    for m in range(1, n+1):
        res = min(res, dist[s][m] + dist[m][a] + dist[m][b])

    return res

n, s, a, b = map(int,input().split())
m = int(input())
fares = [list(map(int,input().split())) for _ in range(m)]
print(solution(n,s,a,b,fares))