import sys
input = sys.stdin.readline

def f():
    N = int(input())

    dp = [0]*50001
    dp[0] = 1
    summ = 0
    for _ in range(N):
        a, b = map(int,input().split())
        summ += a*b
        for i in range(50000, a-1, -1):
            if dp[i-a] == 1:
                for j in range(b):
                    if i + a * j > 50000:
                        break
                    dp[i + a * j] = 1
    return summ % 2 != 1 and dp[summ//2] == 1

for _ in range(3):
    print(int(f()))