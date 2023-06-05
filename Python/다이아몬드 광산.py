import sys
input = sys.stdin.readline

def in_range(x, y):
    return 0 <= x <= R - 1 and 0 <= y <= C - 1

def check_diamond(x, y, length):
    if length == 0:
        return mapp[x][y] == '1'
    
    if in_range(x + (length - 1), y - (length - 1)) and in_range(x + (length - 1), y + (length - 1)):
        return dp_to_right[x + (length - 1)][y - (length - 1)] >= length and dp_to_left[x + (length - 1)][y + (length - 1)] >= length and dp_to_right[x][y] >= length
    
    return False

R, C = map(int, input().split())
mapp = [str(input().rstrip()) for _ in range(R)]

dp_to_left = [[0]*C for _ in range(R)]
# 오른쪽 위 방향으로 조사
start = [[R - 1, y] for y in range(C)] + [[x, 0] for x in range(0, R - 1)]
for x, y in start:
    cur_sequence = 0
    while in_range(x, y):
        if mapp[x][y] == '0':
            cur_sequence = 0
        else:
            cur_sequence += 1
        dp_to_left[x][y] = cur_sequence
        x -= 1
        y += 1

dp_to_right = [[0]*C for _ in range(R)]
# 왼쪽 위 방향으로 조사
start = [[R - 1, y] for y in range(C)] + [[x, C - 1] for x in range(0, R - 1)]
for x, y in start:
    cur_sequence = 0
    while in_range(x, y):
        if mapp[x][y] == '0':
            cur_sequence = 0
        else:
            cur_sequence += 1
        dp_to_right[x][y] = cur_sequence
        x -= 1
        y -= 1

# Solution
result = 0
for x in range(R):
    for y in range(C):
        if mapp[x][y] == '1' and dp_to_left[x][y] > result:
            for test_length in range(dp_to_left[x][y], 0, -1):
                if test_length > result and check_diamond(x, y, test_length):
                    result = test_length
                    break
print(result)