from collections import deque
import sys
input = sys.stdin.readline

def f():
    is_visited = [[False]*N for _ in range(2)]
    q = deque([[0, [0,0]]])
    is_visited[0][0] = True

    while len(q) > 0:
        cur_time, cur_pos = q.popleft()
        x, y = cur_pos

        next_time = cur_time + 1
        next_positions = [
            [x, y+1],
            [x, y-1],
            [(x+1)%2, y+k]
        ]

        for nx, ny in next_positions:
            if ny >= N: return True
            if lines[nx][ny] == "1" and not is_visited[nx][ny] and ny >= next_time:
                q.append([next_time, [nx,ny]])
                is_visited[nx][ny] = True
    
    return False
            

N, k = map(int,input().split())
lines = [input().rstrip(), input().rstrip()]

if f(): print("1")
else: print("0")