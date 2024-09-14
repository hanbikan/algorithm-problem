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
X = list(map(int, input().split()))
P = list(map(int, input().split()))

def bisect_left(lst, v):
    l,r = 0, len(lst)-1
    while l<=r:
        mid = (l+r)//2
        if lst[mid][0] >= v:
            r = mid-1
        else:
            l = mid+1
    return l

pps = []
cur_sum = 0
for i in range(N):
    cur_sum += P[i]
    pps.append([X[i], cur_sum])
pps.sort()

Q = int(input())
for _ in range(Q):
    L, R = map(int, input().split())
    i1 = bisect_left(pps, L) - 1
    i2 = bisect_left(pps, R + 1) - 1
    rps = pps[i2][1] if i2 >= 0 else 0
    lps = pps[i1][1] if i1 >= 0 else 0
    print(rps - lps)