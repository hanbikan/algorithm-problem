from collections import deque
from itertools import combinations
import sys
input = sys.stdin.readline

def is_connected(node_set, node_list):
    is_visited = [False]*(N+1)
    q = deque([node_list[0]])
    is_visited[node_list[0]] = True

    while len(q) > 0:
        cur_node = q.popleft()
        for next_node in graph[cur_node]:
            if not next_node in node_set: continue
            if is_visited[next_node]: continue

            is_visited[next_node] = True
            q.append(next_node)
    
    for node in node_list:
        if not is_visited[node]: return False
    
    return True

def calculate_population_difference(list1, list2):
    sum1, sum2 = 0, 0
    for node in list1:
        sum1 += population[node]
    for node in list2:
        sum2 += population[node]
    
    return abs(sum1 - sum2)

# Input
N = int(input())
population = [0] + list(map(int,input().split()))
graph = {i: [] for i in range(1, N+1)}
for i in range(1, N+1):
    adjacents = list(map(int,input().split()))[1:]
    for adj in adjacents:
        graph[i].append(adj)

# Solution
res = float('inf')
nodes = [i for i in range(1,N+1)]
for select_count in range(1, N//2+1):
    for c in combinations(nodes, select_count):
        set1, set2 = c, set(nodes) - set(c)
        if is_connected(set1, list(set1)) and is_connected(set2, list(set2)):
            res = min(res, calculate_population_difference(list(set1), list(set2)))

if res == float('inf'):
    print(-1)
else:
    print(res)