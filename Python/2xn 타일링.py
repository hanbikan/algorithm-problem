def solution(n):
    DP=[1,2]
    for i in range(2, n):
        DP.append((DP[i-1]+DP[i-2])%10007)
    return DP[n-1]

N=int(input())
print(solution(N))