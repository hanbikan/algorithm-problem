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
H = list(map(int,input().split()))

stack = [-H[-1]] # rev + neg
result = [0] # rev
for i in range(N-2,-1,-1):
    result.append(len(stack))
    index = bisect_left(stack, -H[i])
    if index >= len(stack):
        stack.append(-H[i])
    else:
        stack[index] = -H[i]
        stack = stack[:index+1]
print(*result[::-1])