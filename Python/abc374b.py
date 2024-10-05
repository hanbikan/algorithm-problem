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

S = input().rstrip()
T = input().rstrip()

if S == T:
    print(0)
else:
    index = 0
    flag = True
    while index < len(S) and index < len(T):
        if S[index] != T[index]:
            flag = False
            print(index + 1)
            break
        index += 1

    if flag:
        print(index + 1)