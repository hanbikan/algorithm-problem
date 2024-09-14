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
A = list(map(int, input().split()))

result = 0
sett = set()
cl = N
last = [-1]*(N+1)
for i in range(N):
    if last[A[i]] == -1:
        result += cl * (i + 1)
    else:
        result += cl * (i - last[A[i]])
    sett.add(A[i])
    last[A[i]] = i
    cl -= 1
print(result)