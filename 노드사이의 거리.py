from queue import PriorityQueue
import sys
input = sys.stdin.readline

def f():
    pq = PriorityQueue()
    pq.put([0, a])

    while(not pq.empty()):
        cur_dist, cur_node = pq.get()

        if(cur_node == b):
            return cur_dist

        for dist, next_node in graph[cur_node]:
            if is_visited[next_node]: continue

            pq.put([dist + cur_dist, next_node])
            is_visited[next_node] = True

    return float('inf')

if __name__ == '__main__':
    N, M = map(int, input().split())

    graph = {i:[] for i in range(1, N+1)}
    for _ in range(N-1):
        a, b, d = map(int, input().split())
        graph[a].append([d, b])
        graph[b].append([d, a])

    for _ in range(M):
        a, b = map(int, input().split())
        is_visited = [False]*(N+1)
        is_visited[a] = True
        print(f())