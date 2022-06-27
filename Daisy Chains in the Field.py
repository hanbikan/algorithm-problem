import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N, M = map(int,input().split())
    graph = {i:[] for i in range(1, N+1)}
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    is_visited = [False]*(N+1)
    q = [1]
    is_visited[1] = True
    while(len(q) > 0):
        cur = q.pop(0)

        for n in graph[cur]:
            if not is_visited[n]:
                q.append(n)
                is_visited[n] = True
    
    to_print = []
    for i in range(1, N+1):
        if not is_visited[i]:
            to_print.append(i)

    for str in to_print:
        print(str)
    if len(to_print) == 0:
        print(0)