str1,str2=input(),input()
DP=[0]*len(str2)
for i in range(len(str1)):
    max_dp=0
    for j in range(len(str2)):
        if max_dp<DP[j]: max_dp=DP[j]
        elif str1[i]==str2[j]: DP[j]=max_dp+1
print(max(DP))