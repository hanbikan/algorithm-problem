N = int(input())
for i in range(N):
    tmp = int(input())

    DP = [1,0]
    for j in range(1, tmp+1):
        DP=[DP[1], DP[0]+DP[1]]
    print(DP[0], DP[1])