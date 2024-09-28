import heapq
from bisect import bisect_left, bisect_right
from collections import deque
import collections
import itertools
from itertools import combinations
import sys, math
import random

input = sys.stdin.readline

'''
int(input())
map(int,input().split())
list(map(int,input().split()))
'''

sys.setrecursionlimit(10 ** 6)

N, M = map(int, input().split())
graph = {i: [] for i in range(1, N + 1)}
for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])
    graph[v].append([u, -w])

visited = [False]*(N+1)
x = [0]*(N+1)
for i in range(1,N+1):
    if visited[i]: continue

    q = [i]
    visited[i] = True
    while q:
        u = q.pop()
        for v, w in graph[u]:
            if not visited[v]:
                visited[v] = True
                x[v] = x[u] + w
                q.append(v)
print(*x[1:])

'''
3 2
2 1 1
3 2 6
'''