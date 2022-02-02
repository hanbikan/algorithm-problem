import sys
input = sys.stdin.readline
INF = 1000000007

def solution():
    input()

    res = 0
    prev = 0
    for n in map(int, input().split()):
        prev = ((prev+1)*n) % INF
        res = (res + prev) % INF       

    print(res)

if __name__ == '__main__':
    solution()