import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    K = int(input())
    heap = []
    nums = [0]+list(map(int, input().split()))

    sums = [0]*(K+1)
    for i in range(1, K+1):
        sums[i] = sums[i-1]+nums[i]

    dp = [[0]*(K+1) for _ in range(K+1)]
    for i in range(2, K+1):  # 길이
        for j in range(1, K+2-i):  # 시작지점..K-1~0
            dp[j][j+i-1] = min([dp[j][j+k]+dp[j+k+1][j+i-1]
                                for k in range(i-1)]) + (sums[j+i-1]-sums[j-1])
    print(dp[1][K])
