import sys
input = sys.stdin.readline

# WWWWWWWWWWWW
# BBBBBBBBBBBB
# RRRRRRRRRRRR

def calculate_color_count(start, end):
    res = 0
    for i in range(start):
        for j in range(M):
            if colors[i][j] != 'W':
                res += 1
    
    for i in range(start, end):
        for j in range(M):
            if colors[i][j] != 'B':
                res += 1
    
    for i in range(end, N):
        for j in range(M):
            if colors[i][j] != 'R':
                res += 1
    
    return res

if __name__ == '__main__':
    N, M = map(int, input().split())
    colors = [str(input().rstrip()) for _ in range(N)]

    res = float('inf')
    for start in range(1, N-1):
        for end in range(start+1, N):
            res = min(res, calculate_color_count(start, end))

    print(res)