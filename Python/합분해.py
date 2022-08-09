def solution(N, K):
    RET=0
    if K==2: return N+1
    for i in range(N+1):
        RET+=solution(N-i, K-1)
    return RET

def f1(N,K):
    DP = [[0 for j in range(N+1)] for i in range(K+1)]
    for i in range(N+1): DP[1][i]=1
    for i in range(1, K+1):
        for j in range(N+1):
            for l in range(j+1):
                DP[i][j]+=DP[i-1][j-l]
                DP[i][j]%=1000000000
    for i in DP:
        print(i)
    return DP[K][N]
Input = input()
Input=Input.split()
for i in range(len(Input)):
    Input[i] = int(Input[i])
print(f1(Input[0],Input[1]))