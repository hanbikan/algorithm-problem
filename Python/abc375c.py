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

def print_2d(matrix):
    for m in matrix:
        for c in m:
            print(c, end="")
        print()

N = int(input())
mapp = [list(input().rstrip()) for _ in range(N)]
maps = [[['.']*N for _ in range(N)] for _ in range(4)]
maps[0] = mapp.copy()
for t in range(1, 4):
    for i in range(N):
        for j in range(N):
            maps[t][j][i] = maps[t-1][N-i-1][j]

for t in range(N//2):
    positions = []
    for j in range(t, N-1-t):
        positions.append((t,j))
    for i in range(t, N-1-t):
        positions.append((i,N-1-t))
    for j in range(N-1-t,t,-1):
        positions.append((N-1-t,j))
    for i in range(N-1-t,t,-1):
        positions.append((i,t))

    for x, y in positions:
        mapp[x][y] = maps[(t+1)%4][x][y]

print_2d(mapp)


'''
rotate clockwise 90 deg


6
######
#####.
####..
###...
##....
#.....
'''