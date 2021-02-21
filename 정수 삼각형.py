def solution(listTriangle):
    if len(listTriangle)==1: return listTriangle[0][0]
    DP=[[None for j in range(i+1)] for i in range(len(listTriangle))]

    DP[0][0]=listTriangle[0][0]
    for i in range(1, len(DP)):
        DP[i][0]=DP[i-1][0]+listTriangle[i][0]
        j=0
        for j in range(1, len(DP[i])-1):
            DP[i][j]=max(DP[i-1][j-1], DP[i-1][j])+listTriangle[i][j]
        DP[i][j+1]=DP[i-1][j]+listTriangle[i][j+1]
    
    return max(DP[i])

N=int(input())
Input=[]
for i in range(N):
    tmp=input()
    tmp=tmp.split()
    for j in range(len(tmp)):
        tmp[j]=int(tmp[j])
    Input.append(tmp)

print(solution(Input))