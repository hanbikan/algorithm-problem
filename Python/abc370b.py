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
A = []
for _ in range(N):
    A.append(list(map(int,input().split())))

i = 1
for j in range(1, N + 1):
    if i >= j:
        i = A[i-1][j-1]
    else:
        i = A[j-1][i-1]
print(i)