import sys

input = sys.stdin.readline


def get_line_count():
    global won
    count = 0
    for i in range(3):  # 가로
        if line[i * 3] != '.' and line[i * 3] == line[i * 3 + 1] == line[i * 3 + 2]:
            count += 1
            if won != None and won != line[i * 3]:
                return -1
            won = line[i * 3]
    for j in range(3):  # 세로
        if line[j] != '.' and line[j] == line[j + 3] == line[j + 6]:
            count += 1
            if won != None and won != line[j]:
                return -1
            won = line[j]
    # 대각선
    if line[0] != '.' and line[0] == line[4] == line[8]:
        count += 1
        if won != None and won != line[0]:
            return -1
        won = line[0]
    if line[2] != '.' and line[2] == line[4] == line[6]:
        count += 1
        if won != None and won != line[2]:
            return -1
        won = line[2]
    return count


while True:
    line = str(input().rstrip())
    if line == "end": break

    won = None
    x_count, o_count, blank_count = 0, 0, 0
    for i in range(9):
        if line[i] == 'X':
            x_count += 1
        elif line[i] == 'O':
            o_count += 1
        else:
            blank_count += 1
    line_count = get_line_count()

    valid = False
    if 0 <= x_count - o_count <= 1 and 0 <= line_count <= 2:
        if line_count == 0:
            if x_count == 5 and o_count == 4:
                valid = True
        elif line_count == 1:
            if won == 'X':
                if x_count - o_count == 1:
                    valid = True
            elif won == 'O':
                if x_count == o_count:
                    valid = True
        elif line_count == 2:
            if x_count == 5 and o_count == 4:
                valid = True

    if valid:
        print("valid")
    else:
        print("invalid")
