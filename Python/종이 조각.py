import sys
input = sys.stdin.readline

def calculate_sum(start, end):
    result = 0
    length = (end[0] - start[0]) + (end[1] - start[1]) + 1
    base = 10 ** (length - 1)
    for i in range(start[0], end[0] + 1):
        for j in range(start[1], end[1] + 1):
            result += int(nums[i][j]) * base
            base //= 10
    return result

def check_is_cut(start, end):
    for i in range(start[0], end[0] + 1):
        for j in range(start[1], end[1] + 1):
            if is_cut[i][j]:
                return True
    return False

def set_cut_in_range(start, end, flag):
    for i in range(start[0], end[0] + 1):
        for j in range(start[1], end[1] + 1):
            is_cut[i][j] = flag

def f(start_x, start_y, prefix_sum):
    if start_y >= M:
        f(start_x + 1, 0, prefix_sum)
    elif start_x >= N:
        global result
        result = max(result, prefix_sum)
        return
    elif is_cut[start_x][start_y] or nums[start_x][start_y] == '0':
        f(start_x, start_y + 1, prefix_sum)
    else:
        # row
        for end_y in range(start_y, M):
            start, end = [start_x, start_y], [start_x, end_y]
            if check_is_cut(start, end): continue
            summ = calculate_sum(start, end)
            set_cut_in_range(start, end, True)
            f(start_x, end_y + 1, prefix_sum + summ)
            set_cut_in_range(start, end, False)
        
        # column
        for end_x in range(start_x + 1, N):
            start, end = [start_x, start_y], [end_x, start_y]
            if check_is_cut(start, end): continue
            summ = calculate_sum(start, end)
            set_cut_in_range(start, end, True)
            f(start_x, start_y + 1, prefix_sum + summ)
            set_cut_in_range(start, end, False)

N, M = map(int, input().split())
nums = [] # 각 원소가 문자형임에 유의(e.g. '1')
for _ in range(N):
    strr = input().rstrip()
    nums.append(list(strr))

max_length = max(N, M)
is_cut = [[False] * M for _ in range(N)]
result = 0
f(0, 0, 0)
print(result)