import sys
input = sys.stdin.readline

def f(index, summ):
    res = 0
    if(0.99 <= summ <= 1.01):
        res += 1

    for i in range(index+1, N):
        res += f(i, summ + 1/c[i])

    return res

if __name__ == '__main__':
    N = int(input())
    c = list(map(int,input().split()))
    print(f(-1, 0.0))