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
    flag = True
    to_add = 0
    while i != T:
        if j == i:
            flag = False
            break
        i = (i + 1) % N
        to_add += 1
    if not flag:
        i = indexes[index]
        to_add = 0
        while i != T:
            i = (i + N - 1) % N
            to_add += 1
    result += to_add
    indexes[index] = T
print(result)