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
A = [0] + list(map(int, input().split()))

dp = [[0]*(N+1) for _ in range(2)]
dp[0][1] = 0
dp[1][1] = A[1]
for i in range(2,N+1):
    for b in range(2):
        if b == 0:
            dp[0][i] = max(dp[1][i-1] + A[i] * 2, dp[0][i-1])
        else:
            dp[1][i] = max(dp[0][i-1] + A[i], dp[1][i-1])

print(max(dp[0][-1], dp[1][-1]))
