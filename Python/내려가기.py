import sys, copy
read = sys.stdin.readline

n = int(read().strip())

DP1=list(map(int,read().strip().split()))
DP2=copy.deepcopy(DP1)

for i in range(1, n):
    list_input=list(map(int,read().strip().split()))
    DP1=[max(DP1[0], DP1[1])+list_input[0],max(DP1[0], DP1[1], DP1[2])+list_input[1],max(DP1[1], DP1[2])+list_input[2]]
    DP2=[min(DP2[0], DP2[1])+list_input[0],min(DP2[0], DP2[1], DP2[2])+list_input[1],min(DP2[1], DP2[2])+list_input[2]]

print(max(DP1), min(DP2))