import sys
input = sys.stdin.readline

# ↑ ← ↓ →
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if __name__ == '__main__':
    for _ in range(int(input())):
        max_x, min_x = 0, 0
        max_y, min_y = 0, 0
        
        x, y, dir = 0, 0, 0
        for c in str(input().rstrip()):
            if c == 'F':
                x += dx[dir]
                y += dy[dir]
            elif c == 'B':
                back_dir = (dir + 2) % 4
                x += dx[back_dir]
                y += dy[back_dir]
            elif c == 'L':
                dir = (dir + 1) % 4
            elif c == 'R':
                dir = (dir + 3) % 4
            
            max_x = max(max_x, x)
            min_x = min(min_x, x)
            max_y = max(max_y, y)
            min_y = min(min_y, y)

        print((max_x - min_x)*(max_y - min_y))
    