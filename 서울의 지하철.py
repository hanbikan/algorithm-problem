import sys
input = sys.stdin.readline

def is_linked(a, b):
    for elem in sets[a]:
        if elem in sets[b]:
            return True

    return False

def bfs(start):
    index = 0
    q = [start]
    is_visited = [False]*N
    is_visited[start] = True

    while len(q) > 0:
        nq = []
        while len(q) > 0:
            cur = q.pop(0)

            if cur in ends:
                return index
                
            for nxt in graph[cur]:
                if is_visited[nxt]: continue

                is_visited[nxt] = True
                nq.append(nxt)
        
        index += 1
        q = nq
    
    return -1

if __name__ == '__main__':
    N = int(input())
    sets = [set(list(map(int,input().split()))[1:]) for _ in range(N)]
    end_node = int(input())

    graph = {i:[] for i in range(N)}
    starts = []
    ends = []
    for i in range(N):
        if 0 in sets[i]:
            starts.append(i)
        if end_node in sets[i]:
            ends.append(i)

        for j in range(i+1, N):
            if is_linked(i, j):
                graph[i].append(j)
                graph[j].append(i)
            
    res = float('inf')
    for start in starts:
        res = min(res, bfs(start))
    print(res)