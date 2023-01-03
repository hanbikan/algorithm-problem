from itertools import combinations
import sys
input = sys.stdin.readline

MAX = 100000*20

N = int(input())
s = list(map(int,input().split()))

flags = [False]*(MAX + 1)
for i in range(1, N+1):
    for cb in combinations(s, i):
        flags[sum(cb)] = True

for i in range(1, MAX+1):
    if not flags[i]:
        print(i)
        break