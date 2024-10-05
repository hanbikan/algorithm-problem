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

N, X = map(int, input().split())
w_and_p_pairs = [[]]
for _ in range(N):
    A, P, B, Q = map(int, input().split())
    w_and_p_pairs.append([[A, P], [B, Q]])

l = 0
r = 100 * 10**7
result = 0
while l <= r:
    weight = (l + r) // 2

    price = X
    for i in range(1, N+1):
        w1, p1 = w_and_p_pairs[i][0]
        w2, p2 = w_and_p_pairs[i][1]

        price_to_dec = min(
            math.ceil(weight / w1) * p1,
            math.ceil(weight / w2) * p2,
        )
        if weight % w1 != 0:
            price_to_dec = min(
                price_to_dec,
                math.floor(weight / w1) * p1 + math.ceil((weight - math.floor(weight / w1)) / w2) * p2,
            )
        if weight % w2 != 0:
            price_to_dec = min(
                price_to_dec,
                math.floor(weight / w2) * p2 + math.ceil((weight - math.floor(weight / w2)) / w1) * p1,
            )
        price -= price_to_dec

    if price >= 0:
        l = weight + 1
        result = max(result, weight)
    else:
        r = weight - 1

print(result)