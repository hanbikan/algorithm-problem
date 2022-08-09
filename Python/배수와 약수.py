import sys
input = sys.stdin.readline
FACTOR, MULTIPLE, NEITHER = 0, 1, 2

def solution(n, m):
    if b % a == 0:
        return FACTOR
    elif a % b == 0:
        return MULTIPLE
    else:
        return NEITHER


if __name__ == '__main__':
    a, b = map(int, input().split())
    while not(a == 0 and b == 0):
        res = solution(a, b)
        if res == FACTOR:
            print("factor")
        elif res == MULTIPLE:
            print("multiple")
        else:
            print("neither")

        a, b = map(int, input().split())
