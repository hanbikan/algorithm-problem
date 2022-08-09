def getAmountOfCases(N):
    RET=0
    for a1 in range(N+1):
        remainder=N-a1*1
        a2=0
        while remainder-a2*2>=0:
            cur = remainder-a2*2
            if cur%3==0:
                RET+=C(a1+a2+cur//3, a1)*C(a2+cur//3, a2)
            a2+=1
    return RET

def C(n,r):
    a,b,c=1,1,1
    for i in range(1,n+1):a*=i
    for i in range(1,r+1):b*=i
    for i in range(1,(n-r)+1):c*=i
    return a//(b*c)

T = int(input())
for i in range(T):
    n = int(input())
    print(getAmountOfCases(n))
