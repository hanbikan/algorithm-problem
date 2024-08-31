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

def f():
    if N == 1:
        print(1)
        return
    elif N == 2:
        print(3)
        return

    result = 0
    l = 2
    d = A[1] - A[0]
    for i in range(2, N):
        if A[i] - A[i-1] == d:
            l += 1
        else:
            result += dp[l] - 1
            d = A[i] - A[i-1]
            l = 2
    result += dp[l]
    print(result)


N = int(input())
A = list(map(int, input().split()))

dp = [0] * (N+1)
to_add = 1
for i in range(1, N+1):
    dp[i] = dp[i-1] + to_add
    to_add += 1
f()