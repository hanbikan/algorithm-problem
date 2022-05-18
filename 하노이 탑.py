import sys
input = sys.stdin.readline

def f(n, fr, by, to):
    # fr에 있는 n-1개의 블럭을 by로 옮김
    if(n-1 >= 1): f(n-1, fr, to, by)
    # 가장 밑에 있던 블럭을 to로 옮김
    print(fr+1, to+1)
    # by에 있는 n-1개의 블럭을 to로 옮김
    if(n-1 >= 1): f(n-1, by, fr, to)

if __name__ == '__main__':
    N = int(input())
    print(2**N-1)
    if(N <= 20):
        f(N, 0, 1, 2)
