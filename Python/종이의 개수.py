import sys
input = sys.stdin.readline

def check(start_x, start_y, end_x, end_y):
    cmp = mapp[start_x][start_y]

    for i in range(start_x, end_x):
        for j in range(start_y, end_y):
            if mapp[i][j] != cmp:
                return False
    
    return True

def set_paper_count(start_x, start_y, end_x, end_y):
    global count1, count2, count3

    # 1. Check
    if check(start_x, start_y, end_x, end_y):
        cmp = mapp[start_x][start_y]
        if cmp == -1:
            count1 += 1
        elif cmp == 0:
            count2 += 1
        else:
            count3 += 1
        return

    # 2. Split
    next_length = (end_x - start_x) // 3
    for i in range(3):
        next_start_x = start_x + i * next_length
        next_end_x = next_start_x + next_length
        for j in range(3):
            next_start_y = start_y + j * next_length
            next_end_y = next_start_y + next_length

            set_paper_count(next_start_x, next_start_y, next_end_x, next_end_y)

N = int(input())
mapp = [list(map(int,input().split())) for _ in range(N)]

count1, count2, count3 = 0, 0, 0
set_paper_count(0, 0, N, N)
print(count1)
print(count2)
print(count3)