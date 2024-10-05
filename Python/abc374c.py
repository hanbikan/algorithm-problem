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
map(int,input().split())
list(map(int,input().split()))
'''

sys.setrecursionlimit(10**6)

N = int(input())
K = list(map(int,input().split()))

result = float('inf')
summ = sum(K)
for i in range(1, N // 2 + 1):
    for cb in combinations(K, i):
        scb = sum(cb)
        result = min(result, max(scb, summ - scb))
print(result)