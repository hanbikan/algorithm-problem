N = int(input())
A = {i:True for i in map(int, input().split())}
M = int(input())
for b in map(int, input().split()):
    if(A.get(b)): print(1)
    else: print(0)