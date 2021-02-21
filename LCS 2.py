s1,s2=input(),input()
DP=[[0]*(len(s1)+1) for _ in range(len(s2)+1)]
for i in range(1, len(s2)+1):
    for j in range(1, len(s1)+1):
        if s1[j-1]==s2[i-1]:
            DP[i][j] = DP[i-1][j-1]+1
        else:
            DP[i][j] = max(DP[i][j-1], DP[i-1][j])
print(DP[-1][-1])
i=len(s2)
j=len(s1)
stack=""
while i>0 and j>0:
    if DP[i][j]==DP[i-1][j]:
        i-=1
    elif DP[i][j]==DP[i][j-1]:
        j-=1
    else:
        stack+=s1[j-1]
        i-=1
        j-=1
print(''.join(reversed(stack)))