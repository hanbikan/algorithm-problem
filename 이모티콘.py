S = int(input())
DP = [[-1]*1001 for _ in range(1001)]
DP[1][0] = 0
q=[[1,0]]

# 1. 복사 2. 클립보드 붙이기 3. -1

while q!=[]:
    d, c = map(int, q[0])
    del q[0]
    if d == S: break

    if DP[d][d] == -1:
        DP[d][d] = DP[d][c]+1
        q.append([d, d])
    if d+c<=S and DP[d+c][c] == -1:
        DP[d+c][c] = DP[d][c] + 1
        q.append([d+c, c])
    if d-1>=0 and DP[d-1][c] == -1:
        DP[d-1][c] = DP[d][c] + 1
        q.append([d-1, c])

RET = -1
for i in range(S):
    if DP[S][i] != -1:
        if RET==-1 or RET > DP[S][i]:
            RET = DP[S][i]

print(RET)