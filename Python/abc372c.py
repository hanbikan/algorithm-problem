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

def check(s,e):
    count = 0
    s = max(0,s)
    e = min(N,e)
    for i in range(s,e-2):
        if S[i] == 'A' and S[i+1] == 'B' and S[i+2] == 'C':
            count += 1
    return count

N, Q = map(int,input().split())
S = list(str(input().rstrip()))
res = check(0,N)
for _ in range(Q):
    X, C = map(str, input().split())
    X = int(X) - 1
    pc = check(X-2, X+3)
    S[X] = C
    nc = check(X-2, X+3)
    res += nc - pc
    print(res)