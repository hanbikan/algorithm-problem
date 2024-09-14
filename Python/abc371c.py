import heapq
from bisect import bisect_left, bisect_right
from collections import deque
import collections
import itertools
from itertools import combinations
import sys, math
import random
input = sys.stdin.readline

sys.setrecursionlimit(10**6)

N = int(input())
Mg = int(input())
g = [[False]*(N+1) for _ in range(N+1)]
for _ in range(Mg):
    u,v = map(int, input().split())
    g[u][v] = True
    g[v][u] = True

Mh = int(input())
h = [[False]*(N+1) for _ in range(N+1)]
for _ in range(Mh):
    u,v = map(int, input().split())
    h[u][v] = True
    h[v][u] = True

A = [[0]*(N+1) for i in range(N+1)]
for i in range(1,N):
    nums = list(map(int, input().split()))
    k = 0
    for j in range(i+1, N+1, 1):
        A[i][j] = nums[k]
        k += 1
# h와 g가 동형이 되는 최소 비용(1 <= i < j <= N에서 A[i][j])
min_cost = float('inf')
for pm in itertools.permutations(range(1,N+1), N):
    # 1,2,3,4,5를 pm(ex. 3,2,5,1,4)로 매핑
    node_map = {i:pm[i-1] for i in range(1,N+1)}
    cost = 0
    for i in range(1,N+1):
        for j in range(i+1,N+1):
            if g[node_map[i]][node_map[j]] != h[i][j]:
                cost += A[i][j]
    min_cost = min(min_cost, cost)
print(min_cost)