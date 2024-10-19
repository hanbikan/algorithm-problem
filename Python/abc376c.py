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
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

def f():
    for i in range(N - 1):
        if A[i] > B[i]:
            return -1

    result = A[-1]
    for i in range(N-2, -1, -1):
        if A[i+1] > B[i]:
            break
        else:
            result = A[i]
    return result

print(f())