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
flag = [True]*N
for i in range(M):
    a, b = map(str, input().split())
    a = int(a) - 1
    if b == 'M' and flag[a]:
        print("Yes")
        flag[a] = False
    else:
        print("No")