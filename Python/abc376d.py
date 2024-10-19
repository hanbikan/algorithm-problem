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
map(int, input().split())
list(map(int, input().split()))
'''

sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
graph = {i:[] for i in range(1, N+1)}
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

visited = [False]*(N+1)
visited[1] = True

result = -1
q = [(1, 0)] # node, time
while q:
    node, time = q.pop(0)
    for nxt in graph[node]:
        if nxt == 1:
            result = time + 1
            break

        if visited[nxt]:
            continue

        visited[nxt] = True
        q.append((nxt, time + 1))
    if result != -1:
        break

print(result)