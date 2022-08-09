from queue import PriorityQueue
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    m = int(input())

    # Set a graph
    graph = {i:[] for i in range(1, n+1)}
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    # Solution: BFS
    is_visited = [False]*(n+1)
    is_visited[1] = True
    res = 0
    q = [1]
    move_count = 0

    while len(q) > 0 and move_count < 2:
        nq = []
        while len(q) > 0:
            cur = q.pop(0)
            for next in graph[cur]:
                if not is_visited[next]:
                    is_visited[next] = True
                    nq.append(next)
                    res += 1

        move_count += 1
        q = nq
    
    print(res)