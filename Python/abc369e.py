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

N, M = map(int, input().split())
edges = [[0,0,0]] + [list(map(int,input().split())) for _ in range(M)]

dp = [[float('inf')]*(N+1) for _ in range(N+1)]
for i in range(1,M+1):
    a, b, c = edges[i]
    if c < dp[a][b]:
        dp[a][b] = c
        dp[b][a] = c

for i in range(1,N+1):
    dp[i][i] = 0

# FW
for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            if dp[i][k] + dp[k][j] < dp[i][j]:
                dp[i][j] = dp[i][k] + dp[k][j]

Q = int(input())
for _ in range(Q): # 3000
    K = int(input())
    B = list(map(int, input().split()))

    to_add = 0
    for i in B:
        a, b, c = edges[i]
        to_add += c - dp[a][b]

    result = float('inf')
    for p in itertools.permutations(B, K): # 5! = 120
        for mask in range(1 << K): # 32
            cost, cur = to_add, 1
            for i in range(K): # 5
                a, b, _ = edges[p[i]]
                if mask >> i & 1:
                    cost += dp[cur][a] + dp[a][b]
                    cur = b
                else:
                    cost += dp[cur][b] + dp[b][a]
                    cur = a
            cost += dp[cur][N]
            result = min(result, cost)
    print(result)