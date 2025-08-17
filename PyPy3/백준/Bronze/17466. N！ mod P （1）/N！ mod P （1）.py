import sys
input = sys.stdin.readline

N, P = map(int, input().split())
na = 1
for i in range(2, N + 1):
    na = na * i % P
print(na % P)