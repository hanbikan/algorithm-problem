import heapq
from bisect import bisect_left, bisect_right
from collections import deque
import collections
import itertools
from itertools import combinations
import sys, math
import random
input = sys.stdin.readline

'''
int(input())
map(int, input().split())
list(map(int, input().split()))
'''

sys.setrecursionlimit(10**6)

N = int(input())
cur = (0,0)
result = 0
for _ in range(N):
    X, Y = map(int, input().split())
    result += math.sqrt(math.pow(X - cur[0], 2) + math.pow(Y - cur[1], 2))
    cur = (X, Y)
result += math.sqrt(math.pow(cur[0], 2) + math.pow(cur[1], 2))
print(result)