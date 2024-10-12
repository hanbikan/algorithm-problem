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

S = input().strip()
N = len(S)
sum_count = [[0] * (N + 1) for _ in range(26)]

# 알파벳 개수를 세어주는 부분
for i in range(N):
    for j in range(26):
        sum_count[j][i + 1] = sum_count[j][i]
    sum_count[ord(S[i]) - ord('A')][i + 1] += 1

ans = 0
# 가운데 i를 기준으로 왼쪽과 오른쪽에서 동일한 알파벳의 개수를 세는 부분
for i in range(1, N - 1):
    for j in range(26):
        l = sum_count[j][i]
        r = sum_count[j][N] - sum_count[j][i + 1]
        ans += l * r

print(ans)