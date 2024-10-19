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

N, Q = map(int, input().split())
indexes = [0,1]
result = 0
for _ in range(Q):
    H, T = input().split()
    T = int(T) - 1
    if H == 'L':
        index = 0
    else:
        index = 1

    i = indexes[index]
    j = indexes[(index+1)%2]
    to_add1 = 0
    flag1 = False
    while i != T:
        i = (i + 1) % N
        if j == i:
            flag1 = True
        to_add1 += 1
        if flag1:
            to_add1 += 1

    i = indexes[index]
    to_add2 = 0
    flag2 = False
    while i != T:
        i = (i + N - 1) % N
        if j == i:
            flag2 = True
        to_add2 += 1
        if flag2:
            to_add2 += 1

    if to_add1 < to_add2:
        result += to_add1
        if flag1:
            indexes[(index+1)%2] = (T + 1) % N
    else:
        result += to_add2
        if flag2:
            indexes[(index+1)%2] = (T - 1 + N) % N
    indexes[index] = T
print(result)