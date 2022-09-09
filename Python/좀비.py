from copy import deepcopy
from queue import PriorityQueue
import sys
input = sys.stdin.readline

def set_is_secured():
    global is_secured
    is_visited = [False]*(N+1)
    queue = deepcopy(infected)
    for n in infected:
        is_secured[n] = True
        is_visited[n] = True
    moved = 0

    while len(queue) > 0:
        if moved >= S: break

        next_queue = []
        while len(queue) > 0:
            cur = queue.pop()
            for next in graph[cur]:
                if is_visited[next]: continue

                is_visited[next] = True
                is_secured[next] = True
                next_queue.append(next)

        moved += 1
        queue = next_queue

def f():
    costs = [float('inf')]*(N+1)
    pq = PriorityQueue()
    pq.put([0, 1]) # Cost, Node
    costs[1] = 0

    while not pq.empty():
        cur_cost, cur_node = pq.get()
        for next_node in graph[cur_node]:
            if next_node == N: return cur_cost
            if is_infected[next_node]: continue

            cost_to_add = p if not is_secured[next_node] else q
            next_cost = cur_cost + cost_to_add

            if costs[next_node] > next_cost:
                costs[next_node] = next_cost
                pq.put([next_cost, next_node])

N, M, K, S = map(int,input().split())
p, q = map(int,input().split())
is_infected = [False]*(N+1)
infected = []
for _ in range(K):
    n = int(input())
    infected.append(n)
    is_infected[n] = True

graph = {i: [] for i in range(1, N+1)}
for _ in range(M):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

is_secured = [False]*(N+1)
set_is_secured()

print(f())