def getLCS(str1, str2, str3):
    DP = [[[0]*(len(str1)+1) for _ in range(len(str2)+1)] for _ in range(len(str3)+1)]
    for i in range(1, len(str3)+1):
        for j in range(1, len(str2)+1):
            for k in range(1, len(str1)+1):
                if str3[i-1]==str2[j-1] and str2[j-1]==str1[k-1]:
                    DP[i][j][k] = DP[i-1][j-1][k-1]+1
                else:
                    DP[i][j][k] = max(DP[i-1][j][k], DP[i][j-1][k], DP[i][j][k-1])
    return DP[-1][-1][-1]

str1 = input()
str2 = input()
str3 = input()
print(getLCS(str1, str2, str3))