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

S = list(str(input().rstrip()))
T = list(str(input().rstrip()))
N = len(S)

X = []
while S != T:
    candidates = []
    for i in range(N):
        if S[i] != T[i]:
            tmp = S.copy()
            tmp[i] = T[i]
            candidates.append(tmp)
    candidates.sort()
    X.append(candidates[0])
    S = candidates[0]

print(len(X))
for x in X:
    print(''.join(x))