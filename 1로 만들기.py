N = int(input())
DP = [-1]*(N+1)
DP[0], DP[1] = 0, 0
for i in range(1, N):
    if i+1<=N and (DP[i+1]==-1 or DP[i+1]>DP[i]+1): DP[i+1]=DP[i]+1
    if i*2<=N and (DP[i*2]==-1 or DP[i*2]>DP[i]+1): DP[i*2]=DP[i]+1
    if i*3<=N and (DP[i*3]==-1 or DP[i*3]>DP[i]+1): DP[i*3]=DP[i]+1
print(DP[N])