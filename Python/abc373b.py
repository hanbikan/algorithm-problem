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
map(int,input().split()
list(map(int,input().split())
'''

sys.setrecursionlimit(10**6)

S = str(input().rstrip())
result = 0
cur = S.index('A')
for i in range(1, 26):
    c = chr(ord('A') + i)
    index = S.index(c)

    result += abs(index - cur)
    cur = index
print(result)