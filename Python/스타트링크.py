import sys
from collections import deque
input = sys.stdin.readline

def f():
    if S == G: return 0
    
    # BFS
    dp = [float('inf')]*(F+1)
    q = deque([[0, S]])
    dp[S] = 0

    while len(q) > 0:
        move, floor = q.popleft()

        for k in range(2):
            nx = floor + dx[k]
            if not (1 <= nx <= F): continue
            if dp[nx] != float('inf'): continue

            if nx == G: return move + 1

            q.append([move + 1, nx])
            dp[nx] = move + 1
    
    return "use the stairs"



# 총 F층, 현재 S층, 타겟 G층, 위로 U층, 아래로 D층
F, S, G, U, D = map(int,input().split())
dx = [U, -D]

print(f())