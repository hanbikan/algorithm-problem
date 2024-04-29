import sys
input = sys.stdin.readline

def check_abcdef(c):
    return c == 'A' or c == 'B' or c == 'C' or c == 'D' or c == 'E' or c == 'F'

def test2(str):
    index = 0

    # A 1개 이상
    a_count = 0
    while index < len(str):
        if str[index] == 'A':
            a_count += 1
            index += 1
        else:
            break
    #print("a", a_count)
    if a_count == 0:
        return False

    # F 1개 이상
    f_count = 0
    while index < len(str):
        if str[index] == 'F':
            f_count += 1
            index += 1
        else:
            break
    #print("f", f_count)
    if f_count == 0:
        return False

    # C 1개 이상
    c_count = 0
    while index < len(str):
        if str[index] == 'C':
            c_count += 1
            index += 1
        else:
            break
    #print("c", c_count)
    if c_count == 0:
        return False
    #print(index, len(str))

    # ABCDEF가 0개
    if index >= len(str):
        return True

    # ABCDEF가 1개인 채로 끝남
    if check_abcdef(str[index]) and index == len(str) - 1:
        return True

    return False

def test(str):
    # length exception
    if len(str) <= 2:
        return False

    return test2(str) or test2(str[1:])

T = int(input())
for _ in range(T):
    str = input().rstrip()
    if test(str):
        print("Infected!")
    else:
        print("Good")