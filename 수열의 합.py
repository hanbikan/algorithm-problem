import sys
input = sys.stdin.readline

def is_even(n):
    return n % 2 == 0

if __name__ == '__main__':
    is_successed = False
    N, L = map(int, input().split())

    for i in range(L, 101):
        if is_even(i) and N/i % 1 == 0.5:
            start, end = N//i - i//2 + 1, N//i + i//2 + 1
            if(start < 0): break

            for j in range(start, end):
                print(j ,end=" ")
            is_successed = True
            break
        elif not is_even(i) and N/i == N//i:
            start, end = N//i - i//2, N//i + i//2 + 1
            if(start < 0): break

            for j in range(start, end):
                print(j ,end=" ")
            is_successed = True
            break
    
    if not is_successed:
        print(-1)