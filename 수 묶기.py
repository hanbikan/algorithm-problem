RET = 0
N=int(input())
Pnums, Mnums = [], []
for i in range(N):
    cur = int(input())
    if cur>1: Pnums.append(cur)
    elif cur<=0: Mnums.append(cur)
    else: RET+=cur
Pnums.sort(reverse=True)
Mnums.sort()
for i in range(0, len(Pnums)-1, 2): RET+=Pnums[i]*Pnums[i+1]
if len(Pnums)%2==1: RET += Pnums[-1]
for i in range(0, len(Mnums)-1, 2): RET+=Mnums[i]*Mnums[i+1]
if len(Mnums)%2==1: RET += Mnums[-1]
print(RET)