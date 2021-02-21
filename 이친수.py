def solution(n):
    DP=[None for i in range(n)]
    DP[0] = [0,1]
    for i in range(1, n):
        DP[i] = [DP[i-1][1]+DP[i-1][0], DP[i-1][0]]
    return sum(DP[n-1])

N = int(input())
print(solution(N))