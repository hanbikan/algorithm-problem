import sys                      
input = sys.stdin.readline       
              
if __name__ == '__main__':
    N, a, b = map(int, input().split())

    a += 1
    b += 1

    dp = [0, 1]
    for i in range(2, N+1):
        cur = dp[i-1]+1
        if(i-a>=0): cur = min(cur, dp[i-a]+1)
        if(i-b>=0): cur = min(cur, dp[i-b]+1)

        dp.append(cur)

    print(dp[N])