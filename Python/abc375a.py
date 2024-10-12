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
S = str(input().rstrip())

count = 0
for i in range(N-2):
    if S[i] == '#' and S[i+1] == '.' and S[i+2] == '#':
        count += 1
print(count)