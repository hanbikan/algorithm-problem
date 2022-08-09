import sys
input = sys.stdin.readline

def f(node):
    is_visited[node] = True
    res = 1

    for nxt in graph[node]:
        if not is_visited[nxt]:
            res += f(nxt)

    return res

if __name__ == '__main__':
    for _ in range(int(input())):
        N, M = map(int,input().split())
        graph = {i:[] for i in range(1,N+1)}
        for _ in range(M):
            a, b = map(int,input().split())
            graph[a].append(b)
            graph[b].append(a)
        
        is_visited = [False]*(N+1)

        print(f(1)-1)