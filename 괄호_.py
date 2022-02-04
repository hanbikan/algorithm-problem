import sys
input = sys.stdin.readline 
INF = 1000000007

dp = [0]*5001

def solution(T, Ls):
    dp[0] = 1
    dp[2] = 1

    for i in range(4, max(Ls)+1):
        for j in range(2, i+1):
            dp[i] += dp[j-2]*dp[i-j]
        dp[i] %= INF

    for L in Ls:
        print(dp[L])      

if __name__ == '__main__':
    T = int(input())
    Ls = [int(input()) for _ in range(T)]
    solution(T, Ls)
