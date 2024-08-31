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

H, W, N = map(int, input().split())
has_coin = [[False]*(W+1) for _ in range(H+1)]
nodes = [set() for _ in range(H+1)]
for _ in range(N):
    r, c = map(int, input().split())
    has_coin[r][c] = True
    nodes[r].add(c)

dp = [[[0,[]] for _ in range(W+1)] for _ in range(H+1)]
nodes[1].add(1)
nodes[H].add(W)
for i in range(1, H+1):
    nodes[i].add(1)
    nodes[i].add(W)
    if i == 1:
        for j in range(1, W+1):
            nodes[i].add(j)
    else:
        for j in nodes[i-1]:
            nodes[i].add(j)
    nodes[i] = list(nodes[i])
    nodes[i].sort()

    for k in range(len(nodes[i])):
        j = nodes[i][k]
        if i == j == 1:
            continue

        if i >= 2 and j >= 2:
            left = dp[i][nodes[i][k-1]]
            up = dp[i-1][nodes[i-1][bisect_left(nodes[i-1], j+1) - 1]]
            if up[0] > left[0]:
                dp[i][j] = [up[0], up[1] + ['D']]
            else:
                diff = j - nodes[i][k-1]
                dp[i][j] = [left[0], left[1] + ['R']*diff]
        elif i == 1: # 윗줄
            left = dp[i][nodes[i][k-1]]
            diff = j - nodes[i][k-1]
            dp[i][j] = [left[0], left[1] + ['R']*diff]
        else: # 왼쪽
            dp[i][j] = [dp[i-1][j][0], dp[i-1][j][1] + ['D']]
        if has_coin[i][j]:
            dp[i][j][0] += 1

print(dp[-1][-1][0])
print(''.join(dp[-1][-1][1]))