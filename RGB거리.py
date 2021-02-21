def solution(arr,N):
    DP=[[0 for i in range(3)] for j in range(N)]
    DP[0]=arr[0]
    for i in range(1, N):
        DP[i][0] = min(DP[i-1][1], DP[i-1][2]) + arr[i][0]
        DP[i][1] = min(DP[i-1][0], DP[i-1][2]) + arr[i][1]
        DP[i][2] = min(DP[i-1][1], DP[i-1][0]) + arr[i][2]
    return min(DP[N-1])

N=int(input())
arr=[]
for i in range(N):
    tmp = input()
    tmp = tmp.split()
    for j in range(3):
        tmp[j]=int(tmp[j])
    arr.append(tmp)
print(solution(arr, N))