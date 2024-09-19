import sys
input = sys.stdin.readline

N, K = map(int,input().split())

cur = [i for i in range(1,N+1)]
while len(cur) > K:
    nxt = []
    for i in range(0, len(cur), K):
        nxt.append(cur[i])
        lst = i
    cur = [nxt[-1]] + cur[lst+1:] + nxt[:-1]
print(cur[0])