from collections import deque
from math import sqrt
from operator import is_
import sys
input = sys.stdin.readline

def check_is_prime(number):
    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

def calculate_distance(index1, index2):
    return int(sqrt(
        pow(positions[index1][0] - positions[index2][0], 2) 
        + pow(positions[index1][1] - positions[index2][1], 2)
    ))

x1, y1, x2, y2 = map(int,input().split())
N = int(input())
positions = []
positions.append([x1,y1])
positions.append([x2,y2])
for _ in range(N):
    x, y = map(int,input().split())
    positions.append([x,y])

# 에라토스테네스의 채
is_prime = [True]*(10000)
is_prime[0] = False
is_prime[1] = False
for i in range(2, 10000):
    if is_prime[i]:
        if check_is_prime(i):
            j = 2
            while i*j < 10000:
                is_prime[i*j] = False
                j += 1

graph = {i: [] for i in range(N+2)}
for i in range(N+2):
    for j in range(N+2):
        if i == j: continue
        if is_prime[calculate_distance(i, j)]:
            graph[i].append(j)
            graph[j].append(i)

# Dijkstra
q = deque([[0, 0]])
dists = [float('inf')]*(N+2)
dists[0] = 0
while len(q) > 0:
    cur_dist, cur_node = q.popleft()
    for next_node in graph[cur_node]:
        if next_node == cur_node: continue
        dist_to_next = calculate_distance(cur_node, next_node)
        if not is_prime[dist_to_next]: continue
        next_dist = cur_dist + dist_to_next

        if dists[next_node] > next_dist:
            dists[next_node] = next_dist
            q.append([next_dist, next_node])

res = dists[1]
if res == float('inf'): res = -1
print(res)